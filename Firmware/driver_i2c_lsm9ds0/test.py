import sys
import time
import imu_driver


a = imu_driver.LSM9DS0()

log = open('data.txt', 'w')

log.write("%f\n" % time.time())
for _ in range(int(sys.argv[1])):
  att = a.read()
  log.write("%f,%f,%f\n" % (att.roll,att.pitch,att.yaw))
  
log.write("%f\n" % time.time())
log.close()

