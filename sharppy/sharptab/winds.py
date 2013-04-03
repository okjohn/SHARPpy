''' Wind Manipulation Routines '''
from __future__ import division
import numpy as np
import numpy.ma as ma
from sharppy.sharptab import interp, utils
from sharppy.sharptab.constants import *


__all__ = ['mean_wind', 'mean_wind_npw']


def mean_wind(prof, pbot=850., ptop=250., psteps=20, stu=0, stv=0):
    '''
    Calculates a pressure-weighted mean wind through a layer. The default
    layer is 850 to 200 hPa.

    Parameters
    ----------
    prof: profile object
        Profile Object
    pbot : number (optional; default 850 hPa)
        Pressure of the bottom level (hPa)
    ptop : number (optional; default 250 hPa)
        Pressure of the top level (hPa)
    psteps : integer (optional; default 20)
        Number of steps to loop through (int)
    stu : number (optional; default 0)
        U-component of storm-motion vector
    stv : number (optional; default 0)
        V-component of storm-motion vector

    Returns
    -------
    mnu : number
        U-component
    mnv : number
        V-component

    '''
    if pbot == -1: lower = 850.
    if ptop == -1: upper = 200.
    pinc = int((pbot - ptop) / psteps)
    if pinc < 1:
        u1, v1 = interp.components(pbot, prof)
        u2, v2 = interp.components(ptop, prof)
        u1 = (u1 - stu) * pbot
        v1 = (v1 - stv) * pbot
        u2 = (u2 - stu) * ptop
        v2 = (v2 - stv) * ptop
        usum = u1 + u2
        vsum = v1 + v2
        wgt = pbot + ptop
    else:
        wgt = 0
        usum = 0
        vsum = 0
        for p in range(int(pbot), int(ptop)+1, -pinc):
            utmp, vtmp = interp.components(p, prof)
            usum += (utmp - stu) * p
            vsum += (vtmp - stv) * p
            wgt += p

    return usum / wgt, vsum / wgt


def mean_wind_npw(prof, pbot=850., ptop=250., psteps=20, stu=0, stv=0):
    '''
    Calculates a non-pressure-weighted mean wind through a layer. The default
    layer is 850 to 200 hPa.

    Parameters
    ----------
    prof: profile object
        Profile Object
    pbot : number (optional; default 850 hPa)
        Pressure of the bottom level (hPa)
    ptop : number (optional; default 250 hPa)
        Pressure of the top level (hPa)
    psteps : integer (optional; default 20)
        Number of steps to loop through (int)
    stu : number (optional; default 0)
        U-component of storm-motion vector
    stv : number (optional; default 0)
        V-component of storm-motion vector

    Returns
    -------
    mnu : number
        U-component
    mnv : number
        V-component

    '''
    if pbot == -1: lower = 850.
    if ptop == -1: upper = 200.
    pinc = int((pbot - ptop) / psteps)
    if pinc < 1:
        u1, v1 = interp.components(pbot, prof)
        u2, v2 = interp.components(ptop, prof)
        u1 = (u1 - stu) * pbot
        v1 = (v1 - stv) * pbot
        u2 = (u2 - stu) * ptop
        v2 = (v2 - stv) * ptop
        usum = u1 + u2
        vsum = v1 + v2
        wgt = 2
    else:
        wgt = 0
        usum = 0
        vsum = 0
        for p in range(int(pbot), int(ptop), -pinc):
            utmp, vtmp = interp.components(p, prof)
            usum += (utmp - stu)
            vsum += (vtmp - stv)
            wgt += 1

    return usum / wgt, vsum / wgt
