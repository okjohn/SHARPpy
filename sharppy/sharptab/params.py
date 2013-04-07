''' Thermodynamic Parameter Routines '''
from __future__ import division
import numpy as np
import numpy.ma as ma
from sharppy.sharptab import interp, utils, thermo, winds
from sharppy.sharptab.constants import *


__all__ = ['DefineParcel', 'Parcel']
__all__ += ['k_index', 't_totals', 'c_totals', 'v_totals', 'precip_water']
__all__ += ['temp_lvl', 'max_temp', 'mean_mixratio', 'mean_theta']
__all__ += ['lapse_rate']


class DefineParcel(object):
    '''
    Create a parcel from a supplied profile object.

    Parameters
    ----------
    prof : profile object
        Profile object

    Optional Keywords
        flag : int (default = 1)
            Parcel Selection
                1: Observed Surface Parcel
                2: Forecast Surface Parcel
                3: Most Unstable Parcel
                4: Mean Mixed Layer Parcel
                5: User Defined Parcel
                6: Mean Effective Layer Parcel

    Optional Keywords (Depending on Parcel Selected)
        Parcel (flag) == 1: Observed Surface Parcel
            None

    '''
    def __init__(self, prof, **kwargs):
        self.flag = flag
        if flag == 1:
            self.__sfc(prof)
        elif flag == 2:
            self.__fcst(prof, **kwargs)
        elif flag == 3:
            self.__mu(prof, **kwargs)
        elif flag == 4:
            self.__ml(prof, **kwargs)
        elif flag == 5:
            self.__user(prof, **kwargs)
        elif flag == 6:
            self.__effective(prof, **kwargs)
        else:
            print 'Defaulting to Surface Parcel'
            self.__sfc(prof)


    def __sfc(self, prof):
        '''
        Create a parcel using surface conditions

        '''
        self.desc = 'Surface Parcel'
        self.presval = prof.pres[prof.sfc]
        self.pres = prof.pres[prof.sfc]
        self.tmpc = prof.tmpc[prof.sfc]
        self.dwpc = prof.dwpc[prof.sfc]


    def __fcst(self, prof, **kwargs):
        '''
        Create a parcel using forecast conditions.

        '''
        pass


    def __mu(self, prof, **kwargs):
        '''
        Create the most unstable parcel within the lowest XXX hPa, where
        XXX is supplied. Default XXX is 400 hPa.

        '''
        pass


    def __ml(self, prof, **kwargs):
        '''
        Create a mixed-layer parcel with mixing within the lowest XXX hPa,
        where XXX is supplied. Default is 100 hPa.

        '''
        pass


    def __user(self, prof, **kwargs):
        '''
        Create a user defined parcel.

        '''
        pass


    def __effective(self, prof, **kwargs):
        '''
        Create the mean-effective layer parcel.

        '''
        pass


class Parcel(object):
    '''
    Initialize the parcel variables

    Parameters
    ----------
    prof : profile object
        Profile Object
    lower : number
        Lower-bound (pressure; hPa) that the parcel is lifted
    upper : number
        Upper-bound (pressure; hPa) that the parcel is lifted
    pres : number
        Pressure of the parcel to lift (hPa)
    temp : number
        Temperature of the parcel to lift (C)
    dwpt : number
        Dew Point of the parcel to lift (C)

    '''
    def __init__(self, lower, upper, pres, temp, dwpt,
                 missing=MISSING, **kwargs):
        self.pres = pres
        self.temp = temp
        self.dwpt = dwpt
        self.blayer = lower
        self.tlayer = upper
        self.entrain = 0.
        self.lclpres = missing
        self.lclhght = missing
        self.lfcpres = missing
        self.lfchght = missing
        self.elpres = missing
        self.elhght = missing
        self.mplpres = missing
        self.mplhght = missing
        self.bplus = missing
        self.bminus = missing
        self.bfzl = missing
        self.b3km = missing
        self.b6km = missing
        self.p0c = missing
        self.pm10c = missing
        self.pm20c = missing
        self.pm30c = missing
        self.hght0c = missing
        self.hghtm10c = missing
        self.hghtm20c = missing
        self.hghtm30c = missing
        self.wm10c = missing
        self.wm20c = missing
        self.wm30c = missing
        self.li5 = missing
        self.li3 = missing
        self.brnshear = missing
        self.brn = missing
        self.limax = missing
        self.limaxpres = missing
        self.cap = missing
        self.cappres = missing
        for kw in kwargs: setattr(self, kw, kwargs.get(kw))


def k_index(prof):
    '''
    Calculates the K-Index from a profile object

    Parameters
    ----------
    prof : profile object
        Profile Object

    Returns
    -------
    kind : number
        K-Index

    '''
    t8 = interp.temp(prof, 850.)
    t7 = interp.temp(prof, 700.)
    t5 = interp.temp(prof, 500.)
    td7 = interp.dwpt(prof, 700.)
    td8 = interp.dwpt(prof, 850.)
    return t8 - t5 + td8 - (t7 - td7)


def t_totals(prof):
    '''
    Calculates the Total Totals Index from a profile object

    Parameters
    ----------
    prof : profile object
        Profile Object

    Returns
    -------
    t_totals : number
        Total Totals Index

    '''
    return c_totals(prof) + v_totals(prof)


def c_totals(prof):
    '''
    Calculates the Cross Totals Index from a profile object

    Parameters
    ----------
    prof : profile object
        Profile Object

    Returns
    -------
    c_totals : number
        Cross Totals Index

    '''
    return interp.dwpt(prof, 850.) - interp.temp(prof, 500.)


def v_totals(prof):
    '''
    Calculates the Vertical Totals Index from a profile object

    Parameters
    ----------
    prof : profile object
        Profile Object

    Returns
    -------
    v_totals : number
        Vertical Totals Index

    '''
    return interp.temp(prof, 850.) - interp.temp(prof, 500.)


def precip_water(prof, pbot=None, ptop=400, dp=-1, exact=False):
    '''
    Calculates the precipitable water from a profile object within the
    specified layer. The default layer (lower=-1 & upper=-1) is defined to
    be surface to 400 hPa.

    Parameters
    ----------
    prof : profile object
        Profile Object
    pbot : number (optional; default surface)
        Pressure of the bottom level (hPa)
    ptop : number (optional; default 400 hPa)
        Pressure of the top level (hPa)
    dp : negative integer (optional; default = -1)
        The pressure increment for the interpolated sounding
    exact : bool (optional; default = False)
        Switch to choose between using the exact data (slower) or using
        interpolated sounding at 'dp' pressure levels (faster)

    Returns
    -------
    pwat : number,
        Precipitable Water (in)
    '''
    if not pbot: pbot = prof.pres[prof.sfc]
    if exact:
        ind1 = np.where(pbot > prof.pres)[0].min()
        ind2 = np.where(ptop < prof.pres)[0].max()
        dwpt1 = interp.dwpt(prof, pbot)
        dwpt2 = interp.dwpt(prof, ptop)
        mask = ~prof.dwpc.mask[ind1:ind2+1] * ~prof.pres.mask[ind1:ind2+1]
        dwpt = np.concatenate([[dwpt1], prof.dwpc[ind1:ind2+1][mask], [dwpt2]])
        p = np.concatenate([[pbot], prof.pres[ind1:ind2+1][mask], [ptop]])
    else:
        dp = -1
        p = np.arange(pbot, ptop+dp, dp)
        dwpt = interp.dwpt(prof, p)
    w = thermo.mixratio(p, dwpt)
    return (((w[:-1]+w[1:])/2 * (p[:-1]-p[1:])) * 0.00040173).sum()


def temp_lvl(prof, temp):
    '''
    Calculates the level (hPa) of the first occurrence of the specified
    temperature.

    Parameters
    ----------
    prof : profile object
        Profile Object
    temp : number
        Temperature being searched (C)

    Returns
    -------
    First Level of the temperature (hPa)

    '''
    difft = prof.tmpc - temp
    ind1 = ma.where(difft >= 0)[0]
    ind2 = ma.where(difft <= 0)[0]
    if len(ind1) == 0 or len(ind2) == 0:
        return ma.masked
    inds = np.intersect1d(ind1, ind2)
    if len(inds) > 0:
        return prof.pres[inds][0]
    diff1 = ind1[1:] - ind1[:-1]
    ind = np.where(diff1 > 1)[0] + 1
    try:
        ind = ind.min()
    except:
        ind = ind1[-1]
    return np.exp(np.interp(temp, [prof.tmpc[ind+1], prof.tmpc[ind]],
                  [prof.logp[ind+1], prof.logp[ind]]))


def max_temp(prof, mixlayer=100):
    '''
    Calculates a maximum temperature forecast based on the depth of the mixing
    layer and low-level temperatures

    Parameters
    ----------
    prof : profile object
        Profile Object
    mixlayer : number (optional; default = 100)
        Top of layer over which to "mix" (hPa)

    Returns
    -------
    mtemp : number
        Forecast Maximum Temperature

    '''
    mixlayer = prof.pres[prof.sfc] - mixlayer
    temp = thermo.ctok(interp.temp(prof, mixlayer)) + 2
    return thermo.ktoc(temp * (prof.pres[prof.sfc] / mixlayer)**ROCP)


def mean_mixratio(prof, pbot=None, ptop=None, dp=-1, exact=False):
    '''
    Calculates the mean mixing ratio from a profile object within the
    specified layer.

    Parameters
    ----------
    prof : profile object
        Profile Object
    pbot : number (optional; default surface)
        Pressure of the bottom level (hPa)
    ptop : number (optional; default 400 hPa)
        Pressure of the top level (hPa)
    dp : negative integer (optional; default = -1)
        The pressure increment for the interpolated sounding
    exact : bool (optional; default = False)
        Switch to choose between using the exact data (slower) or using
        interpolated sounding at 'dp' pressure levels (faster)

    Returns
    -------
    Mean Mixing Ratio

    '''
    if not pbot: pbot = prof.pres[prof.sfc]
    if not ptop: ptop = prof.pres[prof.sfc] - 100.
    if not interp.temp(prof, pbot): pbot = prof.pres[prof.sfc]
    if not interp.temp(prof, ptop): return ma.masked
    if exact:
        ind1 = np.where(pbot > prof.pres)[0].min()
        ind2 = np.where(ptop < prof.pres)[0].max()
        dwpt1 = interp.dwpt(prof, pbot)
        dwpt2 = interp.dwpt(prof, ptop)
        mask = ~prof.dwpc.mask[ind1:ind2+1] * ~prof.pres.mask[ind1:ind2+1]
        dwpt = np.concatenate([[dwpt1], prof.dwpc[ind1:ind2+1][mask],
                              [dwpt2]])
        p = np.concatenate([[pbot], prof.pres[ind1:ind2+1][mask], [ptop]])
    else:
        dp = -1
        p = np.arange(pbot, ptop+dp, dp)
        dwpt = interp.dwpt(prof, p)
    w = thermo.mixratio(p, dwpt)
    return ma.average(w, weights=p)


def mean_theta(prof, pbot=None, ptop=None, dp=-1, exact=False):
    '''
    Calculates the mean theta from a profile object within the
    specified layer.

    Parameters
    ----------
    prof : profile object
        Profile Object
    pbot : number (optional; default surface)
        Pressure of the bottom level (hPa)
    ptop : number (optional; default 400 hPa)
        Pressure of the top level (hPa)
    dp : negative integer (optional; default = -1)
        The pressure increment for the interpolated sounding
    exact : bool (optional; default = False)
        Switch to choose between using the exact data (slower) or using
        interpolated sounding at 'dp' pressure levels (faster)

    Returns
    -------
    Mean Theta

    '''
    if not pbot: pbot = prof.pres[prof.sfc]
    if not ptop: ptop = prof.pres[prof.sfc] - 100.
    if not interp.temp(prof, pbot): pbot = prof.pres[prof.sfc]
    if not interp.temp(prof, ptop): return ma.masked
    if exact:
        ind1 = np.where(pbot > prof.pres)[0].min()
        ind2 = np.where(ptop < prof.pres)[0].max()
        theta1 = thermo.theta(interp.pres(prof, pbot), interp.temp(prof, pbot))
        theta2 = thermo.theta(interp.pres(prof, ptop), interp.temp(prof, ptop))
        theta = thermo.theta(prof.pres[ind1:ind2+1], prof.tmpc[ind1:ind2+1])
        mask = ~theta.mask
        theta = np.concatenate([[theta1], theta[mask], [theta2]])
        p = np.concatenate([[pbot], prof.pres[ind1:ind2+1][mask], [ptop]])
    else:
        dp = -1
        p = np.arange(pbot, ptop+dp, dp)
        temp = interp.temp(prof, p)
        theta = thermo.theta(p, temp)
    return ma.average(theta, weights=p)


def lapse_rate(prof, lower, upper, pres=True):
    '''
    Calculates the lapse rate (C/km) from a profile object

    Parameters
    ----------
    prof : profile object
        Profile Object
    lower : number
        Lower Bound of lapse rate
    upper : number
        Upper Bound of lapse rate
    pres : bool (optional; default = True)
        Flag to determine if lower/upper are pressure [True]
        or height [False]

    Returns
    -------
    lapse rate  (float [C/km])
    '''
    if pres:
        p1 = lower
        p2 = upper
        z1 = interp.hght(prof, lower)
        z2 = interp.hght(prof, upper)
    else:
        z1 = interp.to_msl(prof, lower)
        z2 = interp.to_msl(prof, upper)
        p1 = interp.pres(prof, z1)
        p2 = interp.pres(prof, z2)
    tv1 = interp.vtmp(prof, p1)
    tv2 = interp.vtmp(prof, p2)
    return (tv2 - tv1) / (z2 - z1) * -1000.






