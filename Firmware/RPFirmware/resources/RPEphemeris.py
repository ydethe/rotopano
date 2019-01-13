import os

from singleton3 import Singleton

import astropy.units as u
from astropy.units import cds
from astropy.time import Time
from astropy.coordinates import ICRS, get_body, solar_system_ephemeris, SkyCoord, EarthLocation, AltAz


cds.enable()

class RPEphemeris (object, metaclass=Singleton):
    def __init__(self):
        self._lit_messier(catalog=os.path.join(os.path.dirname(__file__), "messier.txt"))
        # solar_system_ephemeris.set('builtin')
        solar_system_ephemeris.set('de430')
        _ = self.getAltAz('mars', lat=0., lon=0., height=0.)

    def _lit_messier(self, catalog='messier.txt'):
        self._messier = []

        f = open(catalog, 'r')
        line = f.readline()
        while not '='*10 in line:
            line = f.readline()

        line = f.readline()
        while line != '':
            elem = line.strip().split()
            if 'x' in elem[10]:
                dx,dy = [float(x.strip()) for x in elem[10].split('x')]
                d_app = max(dx,dy)
            else:
                d_app = float(elem[10])

            dat = {'name':elem[0].strip(),
                   'm_num':elem[1],
                   'ngc_num':elem[2].strip(),
                   'const':elem[3].strip(),
                   'type':elem[4].strip(),
                   'ra_deg':float(elem[5])/3600 + float(elem[6])/60,
                   'dec_deg':float(elem[7])/3600 + float(elem[8])/60,
                   'mag':float(elem[9]),
                   'd_app_arcmin':d_app,
                   'dist_kly':float(elem[11])
                   }
            self._messier.append(dat)

            line = f.readline()

        f.close()

        return self._messier

    def getBody(self, name, t=None):
        lm = [x['name'] for x in self._messier]
        if t is None:
            t = Time.now()
        if name in solar_system_ephemeris.bodies:
            bdy = get_body(name, t)
        elif name in lm:
            i = lm.index(name)
            obj = self._messier[i]
            ra  = obj['ra_deg']*u.deg
            dec = obj['dec_deg']*u.deg
            d   = obj['dist_kly']*u.lyr*1000
            bdy = SkyCoord(frame=ICRS, ra=ra, dec=dec, distance=d, obstime=t)
        return bdy

    def getAltAz(self, name, lat=0., lon=0., height=0., t=None):
        if t is None:
            t = Time.now()
        b = self.getBody(name, t)
        coord = b.transform_to(AltAz(obstime=t,location=EarthLocation(lat=lat*u.deg, lon=lon*u.deg, height=height*u.m),pressure=1*cds.atm))
        if coord.distance.unit == '':
            d = 0.
        else:
            d = coord.distance.value
        return coord.alt.value, coord.az.value, d

    def listBodies(self):
        l = list(solar_system_ephemeris.bodies)
        if 'earth' in l:
            l.remove('earth')
        if 'earth-moon-barycenter' in l:
            l.remove('earth-moon-barycenter')

        lm = [x['name'] for x in self._messier]

        l = l+lm

        return l


if __name__ == '__main__':
    r = RPEphemeris()
    print(r.listBodies())
