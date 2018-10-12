import sys
import imu_driver


a = imu_driver.LSM9DS0()

log = open('data.txt', 'w')

for _ in range(sys.argv[1]):
  r,p,y = a.read()
  log.write("%f,%f,%f\n" % (r,p,y))
  
log.close()
