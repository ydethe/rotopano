from libSystemControl.System import ASystem


class RPSystem (ASystem):
   def __init__(self):
      ASystem.__init__(self, ['pan','tilt'])
      
   def updateSystem(self, u, dt):
      cmd_pan, cmd_tilt = u
      
      
      