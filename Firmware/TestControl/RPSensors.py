from RPFirmware.resources.imu_driver import LSM9DS0
from SystemControl.Sensors import ASensors


class RPSensors (ASensors):
    def __init__(self):
        m = np.zeros(9)
        cov = np.zeros((9,9))
        cov[0,0] = 5.847930521212291e-05
        cov[1,1] = 0.00011570428296016841
        cov[2,2] = 0.00011979610281904613
        cov[3,3] = 8.816001654298385e-06
        cov[4,4] = 3.7248907342466807e-06
        cov[5,5] = 2.844231527812222e-05
        cov[6,6] = 5.847930521212291e-05
        cov[7,7] = 0.00011570428296016841
        cov[8,8] = 0.00011979610281904613
        ASensors.__init__(self, name_of_mes=['gx','gy','gz', 'ax','ay','az', 'mx','my','mz'], mean=m, cov=cov)
        self.imu = LSM9DS0()
        # gx,gy,gz,ax,ay,az,mx,my,mz

    def behavior(self, x, u, t):
        dat = self.imu.read()
        mes = np.array([dat.gyr.x,dat.gyr.y,dat.gyr.z, dat.acc.x,dat.acc.y,dat.acc.z, dat.mag.x,dat.mag.y,dat.mag.z])
        return mes
