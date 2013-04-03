''' Create the Sounding (Profile) Object '''
import numpy as np
import numpy.ma as ma
from sharppy.sharptab import utils
from sharppy.sharptab.constants import MISSING


class Profile(object):
    '''
    The default data class for SHARPpy

    '''
    def __init__(self, **kwargs):
        '''
        Create the sounding data object

        Parameters
        ----------
        Mandatory Keywords
            pres : array_like
                The pressure values (Hectopaschals)
            hght : array_like
                The corresponding height values (Meters)
            tmpc : array_like
                The corresponding temperature values (Celsius)
            dwpc : array_like
                The corresponding dewpoint temperature values (Celsius)

        Optional Keyword Pairs (must use one or the other)
            wdir : array_like
                The direction from which the wind is blowing in
                meteorological degrees
            wspd : array_like
                The speed of the wind

            OR

            u : array_like
                The U-component of the direction from which the wind
                is blowing
            v : array_like
                The V-component of the direction from which the wind
                is blowing.

        Optional Keywords
            missing : number (default: sharppy.sharptab.constants.MISSING)
                The value of the missing flag

        Returns
        -------
        A profile object

        '''
        self.missing = kwargs.get('missing', MISSING)
        self.masked = ma.masked
        self.pres = ma.asanyarray(kwargs.get('pres'))
        self.hght = ma.asanyarray(kwargs.get('hght'))
        self.tmpc = ma.asanyarray(kwargs.get('tmpc'))
        self.dwpc = ma.asanyarray(kwargs.get('dwpc'))
        self.pres[self.pres == self.missing] = ma.masked
        self.hght[self.hght == self.missing] = ma.masked
        self.tmpc[self.tmpc == self.missing] = ma.masked
        self.dwpc[self.dwpc == self.missing] = ma.masked
        self.logp = np.log10(self.pres.copy())
        if 'wdir' in kwargs:
            self.wdir = ma.asanyarray(kwargs.get('wdir'))
            self.wspd = ma.asanyarray(kwargs.get('wspd'))
            self.wdir[self.wdir == self.missing] = ma.masked
            self.wspd[self.wspd == self.missing] = ma.masked
            self.wdir[self.wspd.mask] = ma.masked
            self.wspd[self.wdir.mask] = ma.masked
            self.u, self.v = utils.vec2comp(self.wdir, self.wspd)
        elif 'u' in kwargs:
            self.u = ma.asanyarray(kwargs.get('u'))
            self.v = ma.asanyarray(kwargs.get('v'))
            self.u[self.u == self.missing] = ma.masked
            self.v[self.v == self.missing] = ma.masked
            self.u[self.v.mask] = ma.masked
            self.v[self.u.mask] = ma.masked
            self.wdir, self.wspd = utils.comp2vec(self.u, self.v)
        self.pres.set_fill_value(self.missing)
        self.hght.set_fill_value(self.missing)
        self.tmpc.set_fill_value(self.missing)
        self.dwpc.set_fill_value(self.missing)
        self.wdir.set_fill_value(self.missing)
        self.wspd.set_fill_value(self.missing)
        self.u.set_fill_value(self.missing)
        self.v.set_fill_value(self.missing)
        self.sfc = self.get_sfc()


    def get_sfc(self):
        '''
        Convenience function to get the index of the surface. It is
        determined by finding the lowest level in which a temperature is
        reported.

        Parameters
        ----------
        None

        Returns
        -------
        Index of the surface

        '''
        return np.where(~self.tmpc.mask)[0].min()

