#include <iostream>
#include <stdint.h>
#include "lsm9ds0_yann.h"


LSM9DS0::LSM9DS0() {
    init_ok = true;
    
    xm_fd = i2cOpen(3, LSM9DS0_ADDRESS_ACCELMAG, 0);
    if (xm_fd == -1) {
      std::cerr << "Erreur init I2C XM : " << xm_fd << std::endl;
      init_ok = false;
    }
    
    gy_fd = i2cOpen(3, LSM9DS0_ADDRESS_ACCELMAG, 0);
    if (gy_fd == -1) {
      std::cerr << "Erreur init I2C GYRO : " << gy_fd << std::endl;
      init_ok = false;
    }

    // Enable the accelerometer continous
    write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG1_XM, 0x67); // 100hz XYZ
    write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG5_XM, 0b11110000);
    // enable mag continuous
    write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG7_XM, 0b00000000);
    // enable gyro continuous
    write8(GYROTYPE, LSM9DS0_REGISTER_CTRL_REG1_G, 0x0F); // on XYZ
    // enable the temperature sensor (output rate same as the mag sensor)
    uint8_t tempReg = read8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG5_XM);
    write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG5_XM, tempReg | (1<<7));
  
    // Set default ranges for the various sensors  
    setupAccel(LSM9DS0_ACCELRANGE_2G);
    setupMag(LSM9DS0_MAGGAIN_2GAUSS);
    setupGyro(LSM9DS0_GYROSCALE_245DPS);
    
    if (init_ok)
        std::cout << "Init OK" << std::endl;
}

void LSM9DS0::setupAccel ( const int range )
{
    uint8_t reg = read8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG2_XM);
    reg &= ~(0b00111000);
    reg |= range;
    write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG2_XM, reg );
  
    switch (range)
    {
    case LSM9DS0_ACCELRANGE_2G:
      _accel_mg_lsb = LSM9DS0_ACCEL_MG_LSB_2G;
      break;
    case LSM9DS0_ACCELRANGE_4G:
      _accel_mg_lsb = LSM9DS0_ACCEL_MG_LSB_4G;
      break;
    case LSM9DS0_ACCELRANGE_6G:
      _accel_mg_lsb = LSM9DS0_ACCEL_MG_LSB_6G;
      break;
    case LSM9DS0_ACCELRANGE_8G:
      _accel_mg_lsb = LSM9DS0_ACCEL_MG_LSB_8G;
      break;    
    case LSM9DS0_ACCELRANGE_16G:
      _accel_mg_lsb =LSM9DS0_ACCEL_MG_LSB_16G;
      break;
    }
}

void LSM9DS0::setupMag ( const int gain )
{
  uint8_t reg = read8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG6_XM);
  reg &= ~(0b01100000);
  reg |= gain;
  write8(XMTYPE, LSM9DS0_REGISTER_CTRL_REG6_XM, reg );

  switch(gain)
  {
    case LSM9DS0_MAGGAIN_2GAUSS:
      _mag_mgauss_lsb = LSM9DS0_MAG_MGAUSS_2GAUSS;
      break;
    case LSM9DS0_MAGGAIN_4GAUSS:
      _mag_mgauss_lsb = LSM9DS0_MAG_MGAUSS_4GAUSS;
      break;
    case LSM9DS0_MAGGAIN_8GAUSS:
      _mag_mgauss_lsb = LSM9DS0_MAG_MGAUSS_8GAUSS;
      break;
    case LSM9DS0_MAGGAIN_12GAUSS:
      _mag_mgauss_lsb = LSM9DS0_MAG_MGAUSS_12GAUSS;
      break;
  }
}

void LSM9DS0::setupGyro ( const int scale )
{
  uint8_t reg = read8(GYROTYPE, LSM9DS0_REGISTER_CTRL_REG4_G);
  reg &= ~(0b00110000);
  reg |= scale;
  write8(GYROTYPE, LSM9DS0_REGISTER_CTRL_REG4_G, reg );

  switch(scale)
  {
    case LSM9DS0_GYROSCALE_245DPS:
      _gyro_dps_digit = LSM9DS0_GYRO_DPS_DIGIT_245DPS;
      break;
    case LSM9DS0_GYROSCALE_500DPS:
      _gyro_dps_digit = LSM9DS0_GYRO_DPS_DIGIT_500DPS;
      break;
    case LSM9DS0_GYROSCALE_2000DPS:
      _gyro_dps_digit = LSM9DS0_GYRO_DPS_DIGIT_2000DPS;
      break;
  }
}

void LSM9DS0::readAccel() {
  // Read the accelerometer
  uint8_t buffer[6];
  readBuffer(XMTYPE, 
       0x80 | LSM9DS0_REGISTER_OUT_X_L_A, 
       6, buffer);
  
  uint8_t xlo = buffer[0];
  int16_t xhi = buffer[1];
  uint8_t ylo = buffer[2];
  int16_t yhi = buffer[3];
  uint8_t zlo = buffer[4];
  int16_t zhi = buffer[5];

  std::cout << xlo << ", " << xhi << std::endl;
  
  // Shift values to create properly formed integer (low byte first)
  xhi <<= 8; xhi |= xlo;
  yhi <<= 8; yhi |= ylo;
  zhi <<= 8; zhi |= zlo;
  accelData.x = xhi*_accel_mg_lsb/1000.;
  accelData.y = yhi*_accel_mg_lsb/1000.;
  accelData.z = zhi*_accel_mg_lsb/1000.;
  
}

void LSM9DS0::write8(const bool type, const uint8_t reg, const uint8_t val) {
    int fd, istat;

    if (type == GYROTYPE) {
        fd = gy_fd;
    } else {
        fd = xm_fd;
    }
  
    istat = i2cWriteByteData(fd, reg, val);
    if (istat != 0) {
       std::cerr << "Pb lecture i2cWriteByteData : " << istat << std::endl;
    }
  
}

uint8_t LSM9DS0::read8(const bool type, const uint8_t reg)
{
  int fd, value;

  if (type == GYROTYPE) {
    fd = gy_fd;
  } else {
    fd = xm_fd;
  }

  value = i2cReadByteData(fd, reg);
  if (value < 0) {
     std::cerr << "Pb lecture i2cReadByteData : " << value << std::endl;
  }

  return value;
  
}

uint8_t LSM9DS0::readBuffer(const bool type, const uint8_t reg, const uint8_t len, uint8_t *buffer)
{
  int fd, bytes_read;

  if (type == GYROTYPE) {
    fd = gy_fd;
  } else {
    fd = xm_fd;
  }

   bytes_read = i2cReadI2CBlockData(fd, reg, (char*)buffer, len);
   if (bytes_read != len) {
     std::cerr << "Pb lecture : " << bytes_read << "o lus au lieu de " << len << std::endl;
   }

  return bytes_read;
  
}
