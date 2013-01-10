''' Frequently used functions '''
import numpy as np
import numpy.ma as ma
from sharppy.sharptab.constants import MISSING, TOL

__all__ = ['MS2KTS', 'KTS2MS', 'MS2MPH', 'MPH2MS', 'MPH2KTS', 'KTS2MPH']
__all__ += ['M2FT', 'FT2M']


def MS2KTS(val):
    '''
    Convert meters per second to knots

    Parameters
    ----------
    val : float
        Speed (m/s)

    Returns
    -------
    Val converted to knots (float)

    '''
    return val * 1.94384449


def KTS2MS(val):
    '''
    Convert knots to meters per second

    Parameters
    ----------
    val : float
        Speed (kts)

    Returns
    -------
        Val converted to meters per second (float)

    '''
    return val * 0.514444


def MS2MPH(val):
    '''
    Convert meters per second to miles per hour

    Parameters
    ----------
    val : float
        Speed (m/s)

    Returns
    -------
    Val converted to miles per hour (float)

    '''
    return val * 2.23694


def MPH2MS(val):
    '''
    Convert miles per hour to meters per second

    Parameters
    ----------
    val : float
        Speed (mph)

    Returns
    -------
    Val converted to meters per second (float)

    '''
    return val * 0.44704


def MPH2KTS(val):
    '''
    Convert miles per hour to knots

    Parameters
    ----------
    val : float
        Speed (mph)

    Returns
    -------
    Val converted to knots (float)

    '''
    return val * 0.868976


def KTS2MPH(val):
    '''
    Convert knots to miles per hour

    Parameters
    ----------
    val : float
        Speed (kts)

    Returns
    -------
    Val converted to miles per hour (float)

    '''
    return val * 1.15078


def M2FT(val):
    '''
    Convert meters to feet

    Parameters
    ----------
    val : float
        Distance (m)

    Returns
    -------
        Val converted to feet (float)

    '''
    return val * 3.2808399


def FT2M(val):
    '''
    Convert feet to meters

    Parameters
    ----------
    val : float
        Distance (ft)

    Returns
    -------
        Val converted to meters (float)

    '''
    return val * 0.3048
