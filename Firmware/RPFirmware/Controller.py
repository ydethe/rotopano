from libSystemControl.Controller import AController


class RPController (AController):
   def __init__(self, dt):
      AController.__init__(self, ['cmd_pan', 'cmd_tilt'], dt)
      
   def behavior(self, cons, Xest):
      cons_pan, cons_tilt = cons
      roll,pitch,yaw = Xest
      
      cmd_pan  = -(yaw - cons_pan)
      cmd_tilt = -(pitch- cons_tilt)
      
      u = np.array([cmd_pan, cmd_tilt])
      
      return u
      
      