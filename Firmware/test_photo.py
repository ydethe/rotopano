from RPFirmware.resources.APN import APN
from RPFirmware.resources.EnvoiMail import SendMail


m = APN()
m.takePicture('photo.jpg')
        
SendMail('Test', 'ydethe@gmail.com','ydethe@gmail.com','photo.jpg')
