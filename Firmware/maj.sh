#! /bin/sh


# rsync -avre ssh RPFirmware/ py:mysite/RPFirmware/ --exclude="RPFirmware/__pycache__" --exclude=".DS_Store"
# ssh py "touch /var/www/ydethe_pythonanywhere_com_wsgi.py"

rm -f data.txt
rsync -avre ssh ./ pi:/home/pi/rotopano/Firmware/ --exclude="RPFirmware/__pycache__" --exclude=".DS_Store"
# ssh raspberry "source /home/pi/.zshrc && cd rotopano/Firmware"
# ssh raspberry "source /home/pi/.zshrc && cd rotopano/Firmware && rm -f data.txt && python3 test_clock.py"
# scp raspberry:rotopano/Firmware/data.txt .
# python test_imu.py data.txt
