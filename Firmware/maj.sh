#! /bin/sh


rsync -avre ssh . raspberry:rotopano/Firmware --exclude="RPFirmware/__pycache__" --exclude=".DS_Store"
ssh raspberry ". ~/.zshrc && cd rotopano/Firmware && ./run.sh"
