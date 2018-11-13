from SystemControl.System import ASystem
from RPFirmware.resources.Motor import PanMotor, TiltMotor


class RPSystem (ASystem):
    def __init__(self):
        ASystem.__init__(self, name_of_states=['tilt','pan'])
        self.pan_mot = PanMotor()
        self.tilt_mot = TiltMotor()

        self.pan_mot.setFracStep(16)
        self.tilt_mot.setFracStep(16)

        self.pan_mot.activate()
        self.tilt_mot.activate()

    def updateSystem(self, vel, dt):
        cmd_tilt,cmd_pan = vel

        self.tilt_mot.setSpeed(cmd_tilt)
        self.pan_mot.setSpeed(cmd_pan)
        
