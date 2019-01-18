from multiprocessing import Manager
import os

from singleton3 import Singleton

from RPFirmware.Logger import logger
if 'RP_STUB' in os.environ:
    from RPFirmware.resources.stub.APN import APN
    from RPFirmware.resources.stub.GPS import GPS
    from RPFirmware.resources.stub.RPEphemeris import RPEphemeris
    from RPFirmware.resources.stub.Motor import PanMotor, TiltMotor
#     from RPFirmware.resources.stub.IMU import IMU
else:
    from RPFirmware.Logger import logger
    from RPFirmware.resources.APN import APN
    from RPFirmware.resources.GPS import GPS
    from RPFirmware.resources.RPEphemeris import RPEphemeris
    from RPFirmware.resources.Motor import PanMotor, TiltMotor
#     from RPFirmware.resources.IMU import IMU


class ResourcesManager (object, metaclass=Singleton):
    def __init__(self):
#         self.imu = IMU()
#         logger.info("IMU loaded")
        self.apn = APN()
        logger.info("Camera loaded")
        self.gps = GPS()
        logger.info("GPS loaded")
        self.eph = RPEphemeris()
        logger.info("Ephemeris loaded")
        self.pan = PanMotor()
        logger.info("Pan motor loaded")
        self.tilt = TiltMotor()
        logger.info("Tilt motor loaded")
       