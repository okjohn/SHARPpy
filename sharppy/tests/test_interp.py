import numpy as np
import numpy.ma as ma
import numpy.testing as npt
import sharppy.sharptab.interp as interp
from sharppy.sharptab.utils import vec2comp
from sharppy.sharptab.profile import Profile


p = [1000., 925., 850., 700., 500., 300, 250., 200., 150., 100.]
z = [161., 798., 1496., 3086., 5720., 9370., 10570., 11970., 13700., 16230.]
t = [-9999., 1.2, 9.2, 1.6, -15.5, -43.7, -54.5, -64.1, -64.7, -58.7]
d = [-9999., 1., 9.2, -1.2, -21.5, -50.7, -62.5, -71.1, -71.7, -73.7]
wd = [-9999., 70., 175., 230., 255., 265., 255., 260., 280., 295.]
ws = [-9999., 31.99, 27.99, 25.99, 25.99, 48., 52.99, 75., 77., 39.01]
prof = Profile(pres=p, hght=z, tmpc=t, dwpc=d, wdir=wd, wspd=ws)


def test_pres():
    input_z = 1000.
    correct_p = 902.639252576
    returned_p = interp.pres(input_z, prof)
    npt.assert_almost_equal(returned_p, correct_p)

    input_z = [1000., 3000., 6000.]
    correct_p = np.asarray([902.639252576, 707.38979834, 480.785620453])
    returned_p = interp.pres(input_z, prof)
    npt.assert_almost_equal(returned_p, correct_p)


def test_hght():
    input_p = 900
    correct_z = 1024.17165016
    returned_z = interp.hght(input_p, prof)
    npt.assert_almost_equal(returned_z, correct_z)

    input_p = [900, 800, 600, 400]
    correct_z = np.asarray([1024.17165016, 1992.47263808,
                            4292.73519676, 7314.42659961])
    returned_z = interp.hght(input_p, prof)
    npt.assert_almost_equal(returned_z, correct_z)


def test_temp():
    input_p = 900
    correct_t = 3.7922252167
    returned_t = interp.temp(input_p, prof)
    npt.assert_almost_equal(returned_t, correct_t)

    input_p = [900, 800, 600, 400]
    correct_t = np.asarray([3.7922252167, 6.82692323938,
                            -6.23415788333, -27.8185835915])
    returned_t = interp.temp(input_p, prof)
    npt.assert_almost_equal(returned_t, correct_t)


def test_dwpt():
    input_p = 900
    correct_t = 3.65703084712
    returned_t = interp.dwpt(input_p, prof)
    npt.assert_almost_equal(returned_t, correct_t)

    input_p = [900, 800, 600, 400]
    correct_t = np.asarray([3.65703084712, 5.95263180125,
                            -10.5001991246, -34.2554127969])
    returned_t = interp.dwpt(input_p, prof)
    npt.assert_almost_equal(returned_t, correct_t)


