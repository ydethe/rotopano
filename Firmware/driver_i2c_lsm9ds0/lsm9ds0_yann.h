#include <pigpio.h>

#define LSM9DS0_ADDRESS_ACCELMAG           (0x1D)         // 3B >> 1 = 7bit default
#define LSM9DS0_ADDRESS_GYRO               (0x6B)         // D6 >> 1 = 7bit default
#define LSM9DS0_XM_ID                      (0b01001001)
#define LSM9DS0_G_ID                       (0b11010100)


// Linear Acceleration: mg per LSB
#define LSM9DS0_ACCEL_MG_LSB_2G (0.061F)
#define LSM9DS0_ACCEL_MG_LSB_4G (0.122F)
#define LSM9DS0_ACCEL_MG_LSB_6G (0.183F)
#define LSM9DS0_ACCEL_MG_LSB_8G (0.244F)
#define LSM9DS0_ACCEL_MG_LSB_16G (0.732F) // Is this right? Was expecting 0.488F

// Magnetic Field Strength: gauss range
#define LSM9DS0_MAG_MGAUSS_2GAUSS      (0.08F)
#define LSM9DS0_MAG_MGAUSS_4GAUSS      (0.16F)
#define LSM9DS0_MAG_MGAUSS_8GAUSS      (0.32F)
#define LSM9DS0_MAG_MGAUSS_12GAUSS     (0.48F)

// Angular Rate: dps per LSB
#define LSM9DS0_GYRO_DPS_DIGIT_245DPS      (0.00875F)
#define LSM9DS0_GYRO_DPS_DIGIT_500DPS      (0.01750F)
#define LSM9DS0_GYRO_DPS_DIGIT_2000DPS     (0.07000F)

// Temperature: LSB per degree celsius
#define LSM9DS0_TEMP_LSB_DEGREE_CELSIUS    (8)  // 1°C = 8 25° = 200 etc.

#define GYROTYPE                           (true)
#define XMTYPE                             (false)
#define SPI_CHANNEL                        0
#define SPI_SPEED                          200000
#define SPI_MODE                           0
#define SPI_BUFFER_LEN                     4000

#define LSM9DS0_REGISTER_WHO_AM_I_G        0x0F
#define LSM9DS0_REGISTER_CTRL_REG1_G       0x20
#define LSM9DS0_REGISTER_CTRL_REG3_G       0x22
#define LSM9DS0_REGISTER_CTRL_REG4_G       0x23
#define LSM9DS0_REGISTER_OUT_X_L_G         0x28
#define LSM9DS0_REGISTER_OUT_X_H_G         0x29
#define LSM9DS0_REGISTER_OUT_Y_L_G         0x2A
#define LSM9DS0_REGISTER_OUT_Y_H_G         0x2B
#define LSM9DS0_REGISTER_OUT_Z_L_G         0x2C
#define LSM9DS0_REGISTER_OUT_Z_H_G         0x2D          

#define LSM9DS0_REGISTER_TEMP_OUT_L_XM     0x05
#define LSM9DS0_REGISTER_TEMP_OUT_H_XM     0x06
#define LSM9DS0_REGISTER_STATUS_REG_M      0x07
#define LSM9DS0_REGISTER_OUT_X_L_M         0x08
#define LSM9DS0_REGISTER_OUT_X_H_M         0x09
#define LSM9DS0_REGISTER_OUT_Y_L_M         0x0A
#define LSM9DS0_REGISTER_OUT_Y_H_M         0x0B
#define LSM9DS0_REGISTER_OUT_Z_L_M         0x0C
#define LSM9DS0_REGISTER_OUT_Z_H_M         0x0D
#define LSM9DS0_REGISTER_WHO_AM_I_XM       0x0F
#define LSM9DS0_REGISTER_INT_CTRL_REG_M    0x12
#define LSM9DS0_REGISTER_INT_SRC_REG_M     0x13
#define LSM9DS0_REGISTER_CTRL_REG1_XM      0x20
#define LSM9DS0_REGISTER_CTRL_REG2_XM      0x21
#define LSM9DS0_REGISTER_CTRL_REG5_XM      0x24
#define LSM9DS0_REGISTER_CTRL_REG6_XM      0x25
#define LSM9DS0_REGISTER_CTRL_REG7_XM      0x26
#define LSM9DS0_REGISTER_OUT_X_L_A         0x28
#define LSM9DS0_REGISTER_OUT_X_H_A         0x29
#define LSM9DS0_REGISTER_OUT_Y_L_A         0x2A
#define LSM9DS0_REGISTER_OUT_Y_H_A         0x2B
#define LSM9DS0_REGISTER_OUT_Z_L_A         0x2C
#define LSM9DS0_REGISTER_OUT_Z_H_A         0x2D

#define LSM9DS0_ACCELRANGE_2G              (0b000 << 3)
#define LSM9DS0_ACCELRANGE_4G              (0b001 << 3)
#define LSM9DS0_ACCELRANGE_6G              (0b010 << 3)
#define LSM9DS0_ACCELRANGE_8G              (0b011 << 3)
#define LSM9DS0_ACCELRANGE_16G             (0b100 << 3)

#define LSM9DS0_ACCELDATARATE_POWERDOWN    (0b0000 << 4)
#define LSM9DS0_ACCELDATARATE_3_125HZ      (0b0001 << 4)
#define LSM9DS0_ACCELDATARATE_6_25HZ       (0b0010 << 4)
#define LSM9DS0_ACCELDATARATE_12_5HZ       (0b0011 << 4)
#define LSM9DS0_ACCELDATARATE_25HZ         (0b0100 << 4)
#define LSM9DS0_ACCELDATARATE_50HZ         (0b0101 << 4)
#define LSM9DS0_ACCELDATARATE_100HZ        (0b0110 << 4)
#define LSM9DS0_ACCELDATARATE_200HZ        (0b0111 << 4)
#define LSM9DS0_ACCELDATARATE_400HZ        (0b1000 << 4)
#define LSM9DS0_ACCELDATARATE_800HZ        (0b1001 << 4)
#define LSM9DS0_ACCELDATARATE_1600HZ       (0b1010 << 4)

#define LSM9DS0_MAGGAIN_2GAUSS             (0b00 << 5)  // +/- 2 gauss
#define LSM9DS0_MAGGAIN_4GAUSS             (0b01 << 5)  // +/- 4 gauss
#define LSM9DS0_MAGGAIN_8GAUSS             (0b10 << 5)  // +/- 8 gauss
#define LSM9DS0_MAGGAIN_12GAUSS            (0b11 << 5)  // +/- 12 gauss

#define LSM9DS0_MAGDATARATE_3_125HZ        (0b000 << 2)
#define LSM9DS0_MAGDATARATE_6_25HZ         (0b001 << 2)
#define LSM9DS0_MAGDATARATE_12_5HZ         (0b010 << 2)
#define LSM9DS0_MAGDATARATE_25HZ           (0b011 << 2)
#define LSM9DS0_MAGDATARATE_50HZ           (0b100 << 2)
#define LSM9DS0_MAGDATARATE_100HZ          (0b101 << 2)
      
#define LSM9DS0_GYROSCALE_245DPS           (0b00 << 4)   // +/- 245 degrees per second rotation
#define LSM9DS0_GYROSCALE_500DPS           (0b01 << 4)   // +/- 500 degrees per second rotation
#define LSM9DS0_GYROSCALE_2000DPS          (0b10 << 4)   // +/- 2000 degrees per second rotation
      

class LSM9DS0 {
public:
   LSM9DS0();

   void readAccel();
   
   typedef struct vector_s
    {
      float x;
      float y;
      float z;
    } lsm9ds0Vector_t;
    
    lsm9ds0Vector_t accelData;    // Last read accelerometer data will be available here
    lsm9ds0Vector_t magData;      // Last read magnetometer data will be available here
    lsm9ds0Vector_t gyroData;     // Last read gyroscope data will be available here
    int16_t         temperature;  // Last read temperzture data will be available here
    
private:
   int xm_fd;
   int gy_fd;
   bool init_ok;

   float   _accel_mg_lsb;
   float   _mag_mgauss_lsb;
   float   _gyro_dps_digit;

   void setupAccel ( const int range );
   void setupMag ( const int gain );
   void setupGyro ( const int scale );

   uint8_t read8(const bool type, const uint8_t reg);
   void write8(const bool type, const uint8_t reg, const uint8_t val);
   uint8_t readBuffer(const bool type, const uint8_t reg, const uint8_t len, uint8_t *buffer);
  
};
