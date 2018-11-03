from RPFirmware.resources.APN import APN
from RPFirmware.resources.EnvoiMail import SendMail


m = APN()
apn_path = m.takePicture()
m.downloadPicture(apn_path, 'photo.jpg')
        
SendMail('Test', 'ydethe@gmail.com','ydethe@gmail.com','photo.jpg')


