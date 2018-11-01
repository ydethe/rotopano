from RPFirmware.APN import APN
from RPFirmware.EnvoiMail import SendMail


m = APN()
apn_path = m.takePicture()
m.downloadPicture(apn_path, 'test.jpg')
        
SendMail('Test', 'ydethe@gmail.com','ydethe@gmail.com','test.jpg')


