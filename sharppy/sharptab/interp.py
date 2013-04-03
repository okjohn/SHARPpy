import numpy as np
import numpy.ma as ma
import numpy.testing as npt
from sharppy.sharptab import utils
import sharppy.sharptab.thermo as thermo
from sharppy.sharptab.constants import *


__all__ = ['pres', 'hght']


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
    p : number, numpy
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