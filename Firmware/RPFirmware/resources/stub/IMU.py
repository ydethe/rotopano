from collections import namedtuple
import os

from singleton3 import Singleton

if not 'RP_STUB' in os.environ:
    from imu_driver import LSM9DS0


imu_vector_t_stub = namedtuple('vector', ['x', 'y', 'z'])
imu_data_t_stub = namedtuple('data', ['acc', 'gyr', 'mag', 'qw', 'qx', 'qy', 'qz', 'roll', 'pitch', 'yaw'])

class IMU (object, metaclass=Singleton):
    def __init__(self):
        pass
            
    def read(self) -> "imu_data_t":
        dat = imu_data_t_stub(acc = imu_vector_t_stub(0.,0.,0.),
                              gyr = imu_vector_t_stub(0.,0.,0.),
                              mag = imu_vector_t_stub(0.,0.,0.),
                              qw = 0.,
                              qx = 0.,
                              qy = 0.,
                              qz = 0.,
                              roll = 0.,
                              pitch = 0.,
                              yaw = 0.,
                              )
        return dat
        
    def getPollInterval(self) -> "int":
        return 100
        
        
        