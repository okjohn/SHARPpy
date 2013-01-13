''' Thermodynamic Library '''
import numpy as np
import numpy.ma as ma
from sharppy.sharptab.constants import *

__all__ = ['ftoc', 'ctof', 'ctok', 'ktoc', 'ftok', 'ktof']


def ctof(t):
    '''
    Convert temperature from Celsius to Fahrenheit

    Parameters
    ----------
    t : number, array_like
        The temperature in Celsius

    Returns
    -------
    Temperature in Fahrenheit (number or array_like)

    '''
    return (1.8 * t) + 32.


def ftoc(t):
    '''
    Convert temperature from Fahrenheit to Celsius

    Parameters
    ----------
    t : number, array_like
        The temperature in Fahrenheit

    Returns
    -------
    Temperature in Celsius (number or array_like)

    '''
    return (t - 32.) * (5. / 9.)


def ktoc(t):
    '''
    Convert temperature from Kelvin to Celsius

    Parameters
    ----------
    t : number, array_like
        The temperature in Kelvin

    Returns
    -------
    Temperature in Celsius (number or array_like)

    '''
    return t - ZEROCNK


def ctok(t):
    '''
    Convert temperature from Celsius to Kelvin

    Parameters
    ----------
    t : number, array_like
        The temperature in Celsius

    Returns
    -------
    Temperature in Kelvin (number or array_like)

    '''
    return t + ZEROCNK


def ktof(t):
    '''
    Convert temperature from Kelvin to Fahrenheit

    Parameters
    ----------
    t : number, array_like
        The temperature in Kelvin

    Returns
    -------
    Temperature in Fahrenheit (number or array_like)

    '''
    return ctof(ktoc(t))


def ftok(t):
    '''
    Convert temperature from Fahrenheit to Kelvin

    Parameters
    ----------
    t : number, array_like
        The temperature in Fahrenheit

    Returns
    -------
    Temperature in Kelvin (number or array_like)

    '''
    return ctok(ftoc(t))