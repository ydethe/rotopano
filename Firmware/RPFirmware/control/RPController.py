import numpy as np

from SystemControl.Controller import AController


class RPBangBangController (AController):
    def __init__(self, seuil, cmd):
        AController.__init__(self, 'ctrl', ['cmd_vpan','cmd_vtilt'])
        self.createParameter('seuil', seuil)
        self.createParameter('cmd', cmd)

    @AController.updatemethod
    # @profile
    def update(self, t1 : float, t2 : float, inputs : dict) -> None:
        xest = self.getStateForInput(inputs, 'estimation')
        cons = self.getStateForInput(inputs, 'setpoint')

        # pan_est,bais_vpan_est,tilt_est,biais_vtilt_est = xest
        pan_est,tilt_est = xest
        pan_cons,tilt_cons = cons

        u = np.empty(2)
        if pan_est-pan_cons > self.seuil:
            u[0] = -self.cmd
        elif pan_est-pan_cons < -self.seuil:
            u[0] = self.cmd
        else:
            u[0] = 0.

        if tilt_est-tilt_cons > self.seuil:
            u[1] = -self.cmd
        elif pan_est-pan_cons < -self.seuil:
            u[1] = self.cmd
        else:
            u[1] = 0.

        self.setState(u)


class RPController (AController):
    def __init__(self, P, I):
        AController.__init__(self, 'ctrl', ['cmd_vpan','cmd_vtilt'])
        self.createParameter('Kp', P)
        self.createParameter('Ki', I)

    def reset(self):
        u'''Resets the controller's integrator

        @param val \a float
           Value affected to the integrator

        '''
        AController.reset(self)
        self._int_x = np.zeros(2)

    @AController.updatemethod
    # @profile
    def update(self, t1 : float, t2 : float, inputs : dict) -> None:
        xest = self.getStateForInput(inputs, 'estimation')
        cons = self.getStateForInput(inputs, 'setpoint')

        # pan_est,bais_vpan_est,tilt_est,biais_vtilt_est = xest
        pan_est,tilt_est = xest
        pan_cons,tilt_cons = cons

        u = np.empty(2)
        u[0] = self.Kp*(pan_est-pan_cons) + self.Ki*self._int_x[0]
        self._int_x[0] += (pan_est-pan_cons)*(t2-t1)

        print("Erreur", tilt_est-tilt_cons)
        u[1] = self.Kp*(tilt_est-tilt_cons) + self.Ki*self._int_x[1]
        self._int_x[1] += (tilt_est-tilt_cons)*(t2-t1)

        self.setState(-u)
