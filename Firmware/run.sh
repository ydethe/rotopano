#! /bin/sh


python setup.py install
( cd /home/pi/.berryconda/lib/python3.6/site-packages/RPFirmware-0.0.1-py3.6-linux-armv7l.egg/RPFirmware && ln -s ../imu_driver.cpython-36m-arm-linux-gnueabihf.so _imu_driver.so )
rotopano
