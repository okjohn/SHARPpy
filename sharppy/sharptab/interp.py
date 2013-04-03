import numpy as np
import numpy.ma as ma
import numpy.testing as npt
from sharppy.sharptab import utils
import sharppy.sharptab.thermo as thermo
from sharppy.sharptab.constants import *


def pres(h, prof):
    '''
    Interpolates the given data to calculate a pressure at a given height

    Parameters
    ----------
    h : number
        Height (m) of the level for which pressure is desired
    prof : profile object
        Profile object

    Returns
    -------
    Pressure (hPa) at the given height

    '''
    return 10**np.interp(h, prof.hght, prof.logp)

