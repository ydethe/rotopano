import numpy as np

from SystemControl.Controller import AController


class RPController (AController):
    def __init__(self, P, I, user):
        AController.__init__(self, ['cmd_vpan','cmd_vtilt'])
        self._P = P
        self._I = I
        self.reset()
        self.addSecondarySource(user)

    def reset(self):
        u'''Resets the controller's integrator

        @param val \a float
           Value affected to the integrator

        '''
        self._int_x = np.zeros(2)

    @AController.updatemethod
    def update(self, t1 : float, t2 : float, xest : np.array) -> None:
        cons = self.getSecondarySourceState(0)
        pan_est,bais_vpan_est,tilt_est,biais_vtilt_est = xest
        pan_cons,tilt_cons = cons

        u = np.empty(2)
        u[0] = self._P*(pan_est-pan_cons) + self._I*self._int_x[0]
        self._int_x[0] += (pan_est-pan_cons)*(t2-t1)

        u[1] = self._P*(tilt_est-tilt_cons) + self._I*self._int_x[1]
        self._int_x[1] += (tilt_est-tilt_cons)*(t2-t1)

        self.setState(-u)
