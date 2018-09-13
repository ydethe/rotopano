# The MIT License (MIT)
#
# Copyright (c) 2017, Jack Weatherilt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import math

# The same address is used for both the magnetometer and accelerometer, but
# each has their own variable, to avoid confusion.
LSM9DS0_MAG_ADDRESS     = 0x1D
LSM9DS0_ACCEL_ADDRESS	= 0x1D
LSM9DS0_GYRO_ADDRESS    = 0x6B
                                                                                
# LSM9DS0 gyrometer registers
LSM9DS0_WHO_AM_I_G      = 0x0F
LSM9DS0_CTRL_REG1_G     = 0x20
LSM9DS0_CTRL_REG3_G     = 0x22
LSM9DS0_CTRL_REG4_G     = 0x23
LSM9DS0_OUT_X_L_G       = 0x28
LSM9DS0_OUT_X_H_G       = 0x29
LSM9DS0_OUT_Y_L_G       = 0x2A
LSM9DS0_OUT_Y_H_G       = 0x2B
LSM9DS0_OUT_Z_L_G       = 0x2C
LSM9DS0_OUT_Z_H_G       = 0x2D

# 2D gyroscope low-high register tuple
LSM9DS0_OUT_XYZ_LH_G    = ((LSM9DS0_OUT_X_L_G, LSM9DS0_OUT_X_H_G),
                           (LSM9DS0_OUT_Y_L_G, LSM9DS0_OUT_Y_H_G),
                           (LSM9DS0_OUT_Z_L_G, LSM9DS0_OUT_Z_H_G))

# LSM9DS0 temperature addresses
LSM9DS0_OUT_TEMP_L_XM   = 0x05
LSM9DS0_OUT_TEMP_H_XM   = 0x06

# Temperature low-high register tuple
LSM9DS0_OUT_TEMP_LH = (LSM9DS0_OUT_TEMP_L_XM, LSM9DS0_OUT_TEMP_H_XM)

# Magnetometer addresses
LSM9DS0_STATUS_REG_M    = 0x07
LSM9DS0_OUT_X_L_M       = 0x08
LSM9DS0_OUT_X_H_M       = 0x09
LSM9DS0_OUT_Y_L_M       = 0x0A
LSM9DS0_OUT_Y_H_M       = 0x0B
LSM9DS0_OUT_Z_L_M       = 0x0C
LSM9DS0_OUT_Z_H_M       = 0x0D

# 2D magnetometer low-high register tuple
LSM9DS0_OUT_XYZ_LH_M    = ((LSM9DS0_OUT_X_L_M, LSM9DS0_OUT_X_H_M),
                           (LSM9DS0_OUT_Y_L_M, LSM9DS0_OUT_Y_H_M),
                           (LSM9DS0_OUT_Z_L_M, LSM9DS0_OUT_Z_H_M))

# Shared (mag and accel) addresses
LSM9DS0_WHO_AM_I_XM     = 0x0F
LSM9DS0_INT_CTRL_REG_M  = 0x12
LSM9DS0_INT_SRC_REG_M   = 0x13
LSM9DS0_CTRL_REG1_XM    = 0x20
LSM9DS0_CTRL_REG2_XM    = 0x21
LSM9DS0_CTRL_REG5_XM    = 0x24
LSM9DS0_CTRL_REG6_XM    = 0x25
LSM9DS0_CTRL_REG7_XM    = 0x26

# Accelerometer addresses
LSM9DS0_OUT_X_L_A       = 0x28
LSM9DS0_OUT_X_H_A       = 0x29
LSM9DS0_OUT_Y_L_A       = 0x2A
LSM9DS0_OUT_Y_H_A       = 0x2B
LSM9DS0_OUT_Z_L_A       = 0x2C
LSM9DS0_OUT_Z_H_A       = 0x2D

# 2D accelerometer low-high register tuple
LSM9DS0_OUT_XYZ_LH_A    = ((LSM9DS0_OUT_X_L_A, LSM9DS0_OUT_X_H_A),
                           (LSM9DS0_OUT_Y_L_A, LSM9DS0_OUT_Y_H_A),
                           (LSM9DS0_OUT_Z_L_A, LSM9DS0_OUT_Z_H_A))

# Various settings included in the Arduino library. I haven't used these,
# to keep to a default setting for simplicity, however, users can change
# the settings easily.
LSM9DS0_ACCELRANGE_2G                = 0b000 << 3
LSM9DS0_ACCELRANGE_4G                = 0b001 << 3
LSM9DS0_ACCELRANGE_6G                = 0b010 << 3
LSM9DS0_ACCELRANGE_8G                = 0b011 << 3
LSM9DS0_ACCELRANGE_16G               = 0b100 << 3
 
LSM9DS0_ACCELDATARATE_POWERDOWN      = 0b0000 << 4
LSM9DS0_ACCELDATARATE_3_125HZ        = 0b0001 << 4
LSM9DS0_ACCELDATARATE_6_25HZ         = 0b0010 << 4
LSM9DS0_ACCELDATARATE_12_5HZ         = 0b0011 << 4
LSM9DS0_ACCELDATARATE_25HZ           = 0b0100 << 4
LSM9DS0_ACCELDATARATE_50HZ           = 0b0101 << 4
LSM9DS0_ACCELDATARATE_100HZ          = 0b0110 << 4
LSM9DS0_ACCELDATARATE_200HZ          = 0b0111 << 4
LSM9DS0_ACCELDATARATE_400HZ          = 0b1000 << 4
LSM9DS0_ACCELDATARATE_800HZ          = 0b1001 << 4
LSM9DS0_ACCELDATARATE_1600HZ         = 0b1010 << 4
 
LSM9DS0_MAGGAIN_2GAUSS               = 0b00 << 5
LSM9DS0_MAGGAIN_4GAUSS               = 0b01 << 5
LSM9DS0_MAGGAIN_8GAUSS               = 0b10 << 5
LSM9DS0_MAGGAIN_12GAUSS              = 0b11 << 5

LSM9DS0_MAGDATARATE_3_125HZ          = 0b000 << 2
LSM9DS0_MAGDATARATE_6_25HZ           = 0b001 << 2
LSM9DS0_MAGDATARATE_12_5HZ           = 0b010 << 2
LSM9DS0_MAGDATARATE_25HZ             = 0b011 << 2
LSM9DS0_MAGDATARATE_50HZ             = 0b100 << 2
LSM9DS0_MAGDATARATE_100HZ            = 0b101 << 2

LSM9DS0_GYROSCALE_245DPS             = 0b00 << 4
LSM9DS0_GYROSCALE_500DPS             = 0b01 << 4
LSM9DS0_GYROSCALE_2000DPS            = 0b10 << 4

LSM9DS0_GYRO_SCALEFACTOR = 0.070 * math.pi / 180
LSM9DS0_ACCEL_SCALEFACTOR = 0.00048
LSM9DS0_MAG_SCALEFACTOR = 0.0000732

class LSM9DS0(object):
    # Debug set to false for the moment. Change to find bugs
    def __init__(self, accel_address=LSM9DS0_ACCEL_ADDRESS,
            mag_address=LSM9DS0_MAG_ADDRESS, gyro_address=LSM9DS0_GYRO_ADDRESS,
            I2C=None, busnum=None):
        """Initialise the LSM9DS0 accelerometer, magnetometer and gyroscope.
        """

        # Setup I2C if not already given
        if I2C is None:
            import Adafruit_GPIO.I2C as AdaI2C
            I2C = AdaI2C

        # Each feature is given a call name. Although The magnetometer and
        # accelerometer use the same address, they've been given different
        # names for clarity.
        self.mag    = I2C.get_i2c_device(mag_address, busnum)
        self.accel  = I2C.get_i2c_device(accel_address, busnum)
        self.gyro   = I2C.get_i2c_device(gyro_address, busnum)

        # Magnetometer initialisation
        self.mag.write8(LSM9DS0_CTRL_REG5_XM, 0b11110000) # Temperature sensor enabled, high res mag, 50Hz
        self.mag.write8(LSM9DS0_CTRL_REG6_XM, 0b01100000) # +/- 12 gauss
        self.mag.write8(LSM9DS0_CTRL_REG7_XM, 0b00000000) # Normal mode, continuous-conversion mode

        # Accelerometer initialisation
        self.accel.write8(LSM9DS0_CTRL_REG1_XM, 0b01100111) # 100Hz, XYZ enabled
        self.accel.write8(LSM9DS0_CTRL_REG2_XM, 0b00100000) # +/- 16 g

        # Gyro initialisation
        self.gyro.write8(LSM9DS0_CTRL_REG1_G, 0b00001111) # Normal power mode, XYZ enabled
        self.gyro.write8(LSM9DS0_CTRL_REG4_G, 0b00110000) # Continuous update, 2000 dps

    def readLowHigh(self, i2c_device, lowhigh):
        """Returns signed integer value by reading the given sensor's low and high
        bytes.
        """
        # Unpack low high register pair
        (low, high) = lowhigh

        # Combine the low and high bytes to create new binary value
        # Note the initial 'reading' is postive, so must be converted
        reading = i2c_device.readU8(low) | i2c_device.readU8(high) << 8

        # Convert to negative value if necessary
        if reading > 32767:
            reading -= 65536

        return reading

    def readSensor(self, i2c_device, xyz_lh):
        """Returns (x, y, z) tuple from the given sensor's registers
        """
        xyz = (self.readLowHigh(i2c_device, xyz_lh[0]),  # Pass x lowhigh registers
               self.readLowHigh(i2c_device, xyz_lh[1]),  # Pass y
               self.readLowHigh(i2c_device, xyz_lh[2]))  # Pass z

        return xyz
    
    def readGyro(self):
        """Return gyroscope (x, y, z) tuple"""
        result = self.readSensor(self.gyro, LSM9DS0_OUT_XYZ_LH_G)
        mag_result = tuple([z * LSM9DS0_GYRO_SCALEFACTOR for z in result])
        mag_list = list(mag_result)
        mag_list[2] = -1 * mag_list[2]
        return tuple(mag_list)

    def readMag(self):
        """Return magnetometer (x, y, z) tuple"""
        result = self.readSensor(self.mag, LSM9DS0_OUT_XYZ_LH_M)
        return tuple([z * LSM9DS0_MAG_SCALEFACTOR for z in result])

    def readAccel(self):
        """Returns accelerometer (x, y, z) tuple"""
        result = self.readSensor(self.accel, LSM9DS0_OUT_XYZ_LH_A)
        return tuple([z * LSM9DS0_ACCEL_SCALEFACTOR for z in result])
    

    def read(self):
        """Returns tuple of (gyroxyz, magxyz, accelxyz)"""

        return (self.readGyro(), self.readMag(), self.readAccel())

    # The documentation on reading temperature is not very clear, and it appears
    # that the sensor does not provide an ambient temperature reading, with no
    # absolute value, instead measuring change in temp inside the chip
    def rawTemp(self):
        """Returns temperature value (WARNING: not ambient temperature)"""

        # The temperature values are read from mag/ accel device
        return self.readSensor(self.mag, LSM9DS0_OUT_TEMP_LH)