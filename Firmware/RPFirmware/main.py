from .Sensors import IMU
from .System import RPSystem
from .Interface import RPInterface
from libSystemControl.Estimator import MadgwickFilter
from .Controller import RPController


def main():
   imu = IMU()
   sys = RPSystem()
   dt = 1./50.
   ctl = RPController()
   mf = MadgwickFilter(dt)
   itf = RPInterface(dt, ctl,sys,imu,mf)
   

if __name__ == '__main__':
   main()
   
   
   