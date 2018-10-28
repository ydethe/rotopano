#! /bin/sh


rsync -avre ssh RPFirmware/ py:mysite/RPFirmware/ --exclude="RPFirmware/__pycache__" --exclude=".DS_Store"
ssh py "touch /var/www/ydethe_pythonanywhere_com_wsgi.py"
