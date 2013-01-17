''' Thermodynamic Library '''
from __future__ import division
import numpy as np
import numpy.ma as ma
from sharppy.sharptab.constants import *

__all__ = ['lcltemp', 'theta', 'wobf']
__all__ += ['ftoc', 'ctof', 'ctok', 'ktoc', 'ftok', 'ktof']


def lcltemp(t, td):
    '''
    Returns the temperature (C) of a parcel when raised to its LCL.

    Parameters
    ----------
    t : number, numpy array
        Temperature of the parcel (C)
    td : number, numpy array
        Dewpoint temperature of the parcel (C)

    Returns
    -------
    Temperature (C) of the parcel at it's LCL.

    '''
    s = t - td
    dlt = s * (1.2185 + 0.001278 * t + s * (-0.00219 + 1.173e-5 * s -
        0.0000052 * t))
    return t - dlt


def theta(p, t, p2=1000.):
    '''
    Returns the potential temperature (C) of a parcel.

    Parameters
    ----------
    p : number, numpy array
        The pressure of the parcel (hPa)
    t : number, numpy array
        Temperature of the parcel (C)
    p2 : number, numpy array (default 1000.)
        Reference pressure level (hPa)

    Returns
    -------
    Potential temperature (C)

    '''
    return ((t + ZEROCNK) * (p2 / p)**ROCP) - ZEROCNK


def wobf(t):
    '''
    Implementation of the Wobus Function for computing the moist adiabats.

    Parameters
    ----------
    t : number, numpy array
        Temperature (C)

    Returns
    -------
    Correction to theta (C) for calculation of saturated potential temperature.

    '''
    t -= 20

    npol = 1 + t * (-8.841660499999999e-3 + t * ( 1.4714143e-4
           + t * (-9.671989000000001e-7 + t * (-3.2607217e-8
           + t * (-3.8598073e-10)))))
    npol = 15.13 / (npol**4)

    ppol = t * (4.9618922e-07 + t * (-6.1059365e-09 +
          t * (3.9401551e-11 + t * (-1.2588129e-13 +
          t * (1.6688280e-16)))))
    ppol = 1 + t * (3.6182989e-03 + t * (-1.3603273e-05 + ppol))
    ppol = (29.93 / (ppol**4)) + (0.96 * t) - 14.8

    try:
        correction = np.zeros(t.shape, dtype=np.float64)
        correction[t <= 0] = npol[t <= 0]
        correction[t > 0] = ppol[t > 0]
        return correction
    except AttributeError:
        if t <= 0:
            return npol
        else:
            return ppol


def ctof(t):
    '''
    Convert temperature from Celsius to Fahrenheit

    Parameters
    ----------
    t : number, numpy array
        The temperature in Celsius

    Returns
    -------
    Temperature in Fahrenheit (number or numpy array)

    '''
    return (1.8 * t) + 32.


def ftoc(t):
    '''
    Convert temperature from Fahrenheit to Celsius

    Parameters
    ----------
    t : number, numpy array
        The temperature in Fahrenheit

    Returns
    -------
    Temperature in Celsius (number or numpy array)

    '''
    return (t - 32.) * (5. / 9.)


def ktoc(t):
    '''
    Convert temperature from Kelvin to Celsius

    Parameters
    ----------
    t : number, numpy array
        The temperature in Kelvin

    Returns
    -------
    Temperature in Celsius (number or numpy array)

    '''
    return t - ZEROCNK


def ctok(t):
    '''
    Convert temperature from Celsius to Kelvin

    Parameters
    ----------
    t : number, numpy array
        The temperature in Celsius

    Returns
    -------
    Temperature in Kelvin (number or numpy array)

    '''
    return t + ZEROCNK


def ktof(t):
    '''
    Convert temperature from Kelvin to Fahrenheit

    Parameters
    ----------
    t : number, numpy array
        The temperature in Kelvin

    Returns
    -------
    Temperature in Fahrenheit (number or numpy array)

    '''
    return ctof(ktoc(t))


def ftok(t):
    '''
    Convert temperature from Fahrenheit to Kelvin

    Parameters
    ----------
    t : number, numpy array
        The temperature in Fahrenheit

    Returns
    -------
    Temperature in Kelvin (number or numpy array)

    '''
    return ctok(ftoc(t))