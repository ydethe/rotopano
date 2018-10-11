#! /bin/sh


rsync -rav -e ssh . raspberry:rotopano/Firmware/driver_i2c_lsm9ds0
ssh raspberry ". ~/.zshrc && cd rotopano/Firmware/driver_i2c_lsm9ds0 && make test"
