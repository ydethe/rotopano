from RPFirmware.resources.imu_driver import LSM9DS0
from SystemControl.Sensors import ASensors


class RPSensors (ASensors):
    def __init__(self):
        ASensors.__init__(self, name_of_mes=['ax','ay','az','gx','gy','gz'], mean, cov)
        self.imu = LSM9DS0()
        
