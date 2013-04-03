''' Interpolation Routines '''
import numpy as np
import numpy.ma as ma
import numpy.testing as npt
from sharppy.sharptab import utils
import sharppy.sharptab.thermo as thermo
from sharppy.sharptab.constants import *


__all__ = ['pres', 'hght', 'temp', 'dwpt', 'vtmp', 'components', 'vec']
__all__ += ['agl', 'msl']


def pres(h, prof):
    '''
    Interpolates the given data to calculate a pressure at a given height

    Parameters
    ----------
    h : number, numpy array
        Height (m) of the level for which pressure is desired
    prof : profile object
        Profile object

    Returns
    -------
    Pressure (hPa) at the given height

    '''
    return 10**np.interp(h, prof.hght, prof.logp)


def hght(p, prof):
    '''
    Interpolates the given data to calculate a height at a given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of the level for which height is desired
    prof : profile object
        Profile object

    Returns
    -------
    Height (m) at the given pressure

    '''
    # Note: numpy's interpoloation routine expects the interpoloation
    # routine to be in ascending order. Because pressure decreases in the
    # vertical, we must reverse the order of the two arrays to satisfy
    # this requirement.
    return np.interp(np.log10(p), prof.logp[::-1], prof.hght[::-1])


def temp(p, prof):
    '''
    Interpolates the given data to calculate a temperature at a given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of the level for which temperature is desired
    prof : profile object
        Profile object

    Returns
    -------
    Temperature (C) at the given pressure

    '''
    # Note: numpy's interpoloation routine expects the interpoloation
    # routine to be in ascending order. Because pressure decreases in the
    # vertical, we must reverse the order of the two arrays to satisfy
    # this requirement.
    return np.interp(np.log10(p), prof.logp[::-1], prof.tmpc[::-1])


def dwpt(p, prof):
    '''
    Interpolates the given data to calculate a dew point temperature
    at a given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of the level for which dew point temperature is desired
    prof : profile object
        Profile object

    Returns
    -------
    Dew point tmperature (C) at the given pressure

    '''
    # Note: numpy's interpoloation routine expects the interpoloation
    # routine to be in ascending order. Because pressure decreases in the
    # vertical, we must reverse the order of the two arrays to satisfy
    # this requirement.
    return np.interp(np.log10(p), prof.logp[::-1], prof.dwpc[::-1])


def vtmp(p, prof):
    '''
    Interpolates the given data to calculate a virtual temperature
    at a given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of the level for which virtual temperature is desired
    prof : profile object
        Profile object

    Returns
    -------
    Virtual tmperature (C) at the given pressure

    '''
    t = temp(p, prof)
    td = dwpt(p, prof)
    try:
        vt = []
        for pp,tt,tdtd in zip(p, t, td):
            vt.append(thermo.virtemp(pp, tt, tdtd))
        return np.asanyarray(vt)
    except TypeError:
        return thermo.virtemp(p, t, td)


def components(p, prof):
    '''
    Interpolates the given data to calculate the U and V components at a
    given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of a level
    prof : profile object
        Profile object

    Returns
    -------
    U and V components at the given pressure
    '''
    # Note: numpy's interpoloation routine expects the interpoloation
    # routine to be in ascending order. Because pressure decreases in the
    # vertical, we must reverse the order of the two arrays to satisfy
    # this requirement.
    U = np.interp(np.log10(p), prof.logp[::-1], prof.u[::-1])
    V = np.interp(np.log10(p), prof.logp[::-1], prof.v[::-1])
    return U, V


def vec(p, prof):
    '''
    Interpolates the given data to calculate the wind direction and speed
    at a given pressure

    Parameters
    ----------
    p : number, numpy array
        Pressure (hPa) of a level
    prof : profile object
        Profile object

    Returns
    -------
    Wind direction and magnitude at the given pressure
    '''
    U, V = components(p, prof)
    return utils.comp2vec(U, V)


def agl(h, prof):
    '''
    Convert a height from mean sea-level (MSL) to above ground-level (AGL)

    Parameters
    ----------
    h : number, numpy array
        Height of a level
    prof : profile object
        Profile object

    Returns
    -------
    Converted height

    '''
    return h - prof.hght[prof.sfc]


def msl(h, prof):
    '''
    Convert a height from above ground-level (AGL) to mean sea-level (MSL)

    Parameters
    ----------
    h : number, numpy array
        Height of a level
    prof : profile object
        Profile object

    Returns
    -------
    Converted height

    '''
    return h + prof.hght[prof.sfc]










