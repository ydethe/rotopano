import sys
import time
import imu_driver


a = imu_driver.LSM9DS0()

log = open('data.txt', 'w')

log.write("%f\n" % time.time())
for _ in range(int(sys.argv[1])):
  r,p,y = a.read()
  print(r,p,y)
  log.write("%f,%f,%f\n" % (r,p,y))
  
log.write("%f\n" % time.time())
log.close()

