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
print prof.u
print prof.v

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


def test_vtmp():
    input_p = 900
    correct_v = 4.722189142078207
    returned_v = interp.vtmp(input_p, prof)
    npt.assert_almost_equal(returned_v, correct_v)

    input_p = [900, 800, 600, 400]
    correct_v = np.asarray([4.722189142078207, 8.069359717080374,
                            -5.769345740514382, -27.74007032980404])
    returned_v = interp.vtmp(input_p, prof)
    npt.assert_almost_equal(returned_v, correct_v)


def test_components():
    input_p = 900
    correct_u, correct_v = -21.1106953677, 1.63907594278
    correct = [correct_u, correct_v]
    returned = interp.components(input_p, prof)
    npt.assert_almost_equal(returned, correct)

    input_p = [900, 800, 600, 400]
    correct_u = np.asarray([-21.1106953677, 4.53891277421,
                            22.289483447, 35.026084823])
    correct_v = np.asarray([1.63907594278, 24.3933682556,
                            12.1341348539, 5.61574926111])
    correct = [correct_u, correct_v]
    returned = interp.components(input_p, prof)
    npt.assert_almost_equal(returned, correct)


def test_vec():
    input_p = 900
    correct_wdir, correct_wspd = 94.43965025418073, 21.174230301336348
    correct = [correct_wdir, correct_wspd]
    returned = interp.vec(input_p, prof)
    npt.assert_almost_equal(returned, correct)

    input_p = [900, 800, 600, 400]
    correct_wdir = np.asarray([94.43965025418073, 190.54057243918774,
                               241.43664290047258, 260.8912611327822])
    correct_wspd = np.asarray([21.174230301336348, 24.812056424754488,
                               25.378303745260787, 35.473416212590074])
    correct = [correct_wdir, correct_wspd]
    returned = interp.vec(input_p, prof)
    npt.assert_almost_equal(returned, correct)


def test_agl():
    input_z = 1000.
    correct_agl = 202.
    returned_agl = interp.agl(input_z, prof)
    npt.assert_almost_equal(returned_agl, correct_agl)

    input_z = [1000., 3000., 6000.]
    correct_agl = [202., 2202., 5202]
    returned_agl = interp.agl(input_z, prof)
    npt.assert_almost_equal(returned_agl, correct_agl)


def test_msl():
    input_z = 1000.
    correct_agl = 1798.
    returned_agl = interp.msl(input_z, prof)
    npt.assert_almost_equal(returned_agl, correct_agl)

    input_z = [1000., 3000., 6000.]
    correct_agl = [1798., 3798., 6798]
    returned_agl = interp.msl(input_z, prof)
    npt.assert_almost_equal(returned_agl, correct_agl)



