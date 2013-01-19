import numpy as np
import numpy.ma as ma
import numpy.testing as npt
import sharppy.sharptab.thermo as thermo
from sharppy.sharptab.constants import *


def test_ctof():
    # single pass
    input_c = 0
    correct_f = 32
    returned_f = thermo.ctof(input_c)
    npt.assert_almost_equal(returned_f, correct_f)

    # array_like pass
    input_c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    input_c = np.asanyarray(input_c)
    correct_f = [32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212]
    correct_f = np.asanyarray(correct_f)
    returned_f = thermo.ctof(input_c)
    npt.assert_almost_equal(returned_f, correct_f)

    # single masked
    input_c = ma.masked
    correct_f = ma.masked
    returned_f = thermo.ctof(input_c)
    npt.assert_(type(returned_f), type(correct_f))

    # array_like pass
    inds = [0, 5, 7]
    input_c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    input_c = np.ma.asanyarray(input_c)
    correct_f = [32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212]
    correct_f = np.ma.asanyarray(correct_f)
    input_c[inds] = ma.masked
    correct_f[inds] = ma.masked
    returned_f = thermo.ctof(input_c)
    npt.assert_almost_equal(returned_f, correct_f)


def test_ftoc():
    # single pass
    input_f = 32
    correct_c = 0
    returned_c = thermo.ftoc(input_f)
    npt.assert_almost_equal(returned_c, correct_c)

    # array_like pass
    input_f = [32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212]
    input_f = np.asanyarray(input_f)
    correct_c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    correct_c = np.asanyarray(correct_c)
    returned_c = thermo.ftoc(input_f)
    npt.assert_almost_equal(returned_c, correct_c)

    # single masked
    input_f = ma.masked
    correct_c = ma.masked
    returned_c = thermo.ftoc(input_f)
    npt.assert_(type(returned_c), type(correct_c))

    # array_like pass
    inds = [0, 5, 7]
    input_f = [32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212]
    input_f = np.ma.asanyarray(input_f)
    correct_c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    correct_c = np.ma.asanyarray(correct_c)
    input_f[inds] = ma.masked
    correct_c[inds] = ma.masked
    returned_c = thermo.ftoc(input_f)
    npt.assert_almost_equal(returned_c, correct_c)


def test_ktoc():
    # single pass
    input_k = 0
    correct_c = -273.15
    returned_c = thermo.ktoc(input_k)
    npt.assert_almost_equal(returned_c, correct_c)

    # array_like pass
    input_k = [0, 50, 100, 150, 200, 250, 300]
    input_k = np.asanyarray(input_k)
    correct_c = [-273.15, -223.15, -173.15, -123.15, -73.15, -23.15, 26.85]
    correct_c = np.asanyarray(correct_c)
    returned_c = thermo.ktoc(input_k)
    npt.assert_almost_equal(returned_c, correct_c)

    # single masked
    input_k = ma.masked
    correct_c = ma.masked
    returned_c = thermo.ktoc(input_k)
    npt.assert_(type(returned_c), type(correct_c))

    # array_like pass
    inds = [0, 2, 3]
    input_k = [0, 50, 100, 150, 200, 250, 300]
    input_k = np.ma.asanyarray(input_k)
    correct_c = [-273.15, -223.15, -173.15, -123.15, -73.15, -23.15, 26.85]
    correct_c = np.ma.asanyarray(correct_c)
    input_k[inds] = ma.masked
    correct_c[inds] = ma.masked
    returned_c = thermo.ktoc(input_k)
    npt.assert_almost_equal(returned_c, correct_c)


def test_ctok():
    # single pass
    input_c = -273.15
    correct_k = 0
    returned_k = thermo.ctok(input_c)
    npt.assert_almost_equal(returned_k, correct_k)

    # array_like pass
    input_c = [-273.15, -223.15, -173.15, -123.15, -73.15, -23.15, 26.85]
    input_c = np.asanyarray(input_c)
    correct_k = [0, 50, 100, 150, 200, 250, 300]
    correct_k = np.asanyarray(correct_k)
    returned_k = thermo.ctok(input_c)
    npt.assert_almost_equal(returned_k, correct_k)

    # single masked
    input_c = ma.masked
    correct_k = ma.masked
    returned_k = thermo.ctok(input_c)
    npt.assert_(type(returned_k), type(correct_k))

    # array_like pass
    inds = [0, 2, 3]
    input_c = [-273.15, -223.15, -173.15, -123.15, -73.15, -23.15, 26.85]
    input_c = np.ma.asanyarray(input_c)
    correct_k = [0, 50, 100, 150, 200, 250, 300]
    correct_k = np.ma.asanyarray(correct_k)
    input_c[inds] = ma.masked
    correct_k[inds] = ma.masked
    returned_k = thermo.ctok(input_c)
    npt.assert_almost_equal(returned_k, correct_k)


def test_ktof():
    # single pass
    input_k = 0
    correct_f = -459.67
    returned_f = thermo.ktof(input_k)
    npt.assert_almost_equal(returned_f, correct_f)

    # array_like pass
    input_k = [0, 50, 100, 150, 200, 250, 300]
    input_k = np.asanyarray(input_k)
    correct_f = [-459.67, -369.67, -279.67, -189.67, -99.67, -9.67, 80.33]
    correct_f = np.asanyarray(correct_f)
    returned_f = thermo.ktof(input_k)
    npt.assert_almost_equal(returned_f, correct_f)

    # single masked
    input_k = ma.masked
    correct_f = ma.masked
    returned_f = thermo.ktof(input_k)
    npt.assert_(type(returned_f), type(correct_f))

    # array_like pass
    inds = [0, 2, 3]
    input_k = [0, 50, 100, 150, 200, 250, 300]
    input_k = np.ma.asanyarray(input_k)
    correct_f = [-459.67, -369.67, -279.67, -189.67, -99.67, -9.67, 80.33]
    correct_f = np.ma.asanyarray(correct_f)
    input_k[inds] = ma.masked
    correct_f[inds] = ma.masked
    returned_f = thermo.ktof(input_k)
    npt.assert_almost_equal(returned_f, correct_f)


def test_ftok():
    # single pass
    input_f = -459.67
    correct_k = 0
    returned_k = thermo.ftok(input_f)
    npt.assert_almost_equal(returned_k, correct_k)

    # array_like pass
    input_f = [-459.67, -369.67, -279.67, -189.67, -99.67, -9.67, 80.33]
    input_f = np.asanyarray(input_f)
    correct_k = [0, 50, 100, 150, 200, 250, 300]
    correct_k = np.asanyarray(correct_k)
    returned_k = thermo.ftok(input_f)
    npt.assert_almost_equal(returned_k, correct_k)

    # single masked
    input_f = ma.masked
    correct_k = ma.masked
    returned_k = thermo.ftok(input_f)
    npt.assert_(type(returned_k), type(correct_k))

    # array_like pass
    inds = [0, 2, 3]
    input_f = [-459.67, -369.67, -279.67, -189.67, -99.67, -9.67, 80.33]
    input_f = np.ma.asanyarray(input_f)
    correct_k = [0, 50, 100, 150, 200, 250, 300]
    correct_k = np.ma.asanyarray(correct_k)
    input_f[inds] = ma.masked
    correct_k[inds] = ma.masked
    returned_k = thermo.ftok(input_f)
    npt.assert_almost_equal(returned_k, correct_k)


def test_theta():
    # single
    input_p = 940
    input_t = 5
    input_p2 = 1000.
    correct_theta = 9.961049492262532
    returned_theta = thermo.theta(input_p, input_t, input_p2)
    npt.assert_almost_equal(returned_theta, correct_theta)

    # array
    input_p = np.asarray([940, 850])
    input_t = np.asarray([5, 10])
    input_p2 = np.asarray([1000., 1000.])
    correct_theta = [9.961049492262532, 23.457812111895066]
    returned_theta = thermo.theta(input_p, input_t, input_p2)
    npt.assert_almost_equal(returned_theta, correct_theta)


def test_wobf():
    input_t = 10
    correct_c = 10.192034543230415
    returned_c = thermo.wobf(input_t)
    npt.assert_almost_equal(returned_c, correct_c)

    input_t = [10, 0, -10]
    input_t = np.asanyarray(input_t)
    correct_c = [10.192034543230415, 6.411053315058521, 3.8633154447163114]
    correct_c = np.asanyarray(correct_c)
    returned_c = thermo.wobf(input_t)
    npt.assert_almost_equal(returned_c, correct_c)


def test_lcltemp():
    input_t = 10
    input_td = 5
    correct_t = 3.89818375
    returned_t = thermo.lcltemp(input_t, input_td)
    npt.assert_almost_equal(returned_t, correct_t)

    input_t = np.asanyarray([20, 10, 0, -5])
    input_td = np.asanyarray([15, 8, -1, -10])
    correct_t = [13.83558375, 7.54631416, -1.21632173, -11.00791625]
    correct_t = np.asanyarray(correct_t)
    returned_t = thermo.lcltemp(input_t, input_td)
    npt.assert_almost_equal(returned_t, correct_t)


def test_thalvl():
    input_theta = 10
    input_t = 5
    correct_p = 939.5475008003834
    returned_p = thermo.thalvl(input_theta, input_t)
    npt.assert_almost_equal(returned_p, correct_p)

    input_theta = np.asanyarray([5, 12, 25])
    input_t = np.asanyarray([5, 10, 0.])
    correct_p = [1000., 975.6659847653189, 736.0076986893786]
    correct_p = np.asanyarray(correct_p)
    returned_p = thermo.thalvl(input_theta, input_t)
    npt.assert_almost_equal(returned_p, correct_p)


def test_drylift():
    input_p = 950
    input_t = 30
    input_td = 25
    correct_p = 883.4367363248148
    correct_t = 23.77298375
    returned_p, returned_t = thermo.drylift(input_p, input_t, input_td)
    npt.assert_almost_equal(returned_p, correct_p)
    npt.assert_almost_equal(returned_t, correct_t)

    input_p = np.asarray([950, 975, 1013, 900])
    input_t = np.asarray([30, 10, 22, 40])
    input_td = np.asarray([25, -10, 18, 0])
    correct_p = np.asarray([883.4367363248148, 716.8293994988512,
                            954.7701032005202, 504.72627541064145])
    correct_t = np.asarray([23.77298375, -13.822639999999996,
                            17.04965568, -7.6987199999999945])
    returned_p, returned_t = thermo.drylift(input_p, input_t, input_td)
    npt.assert_almost_equal(returned_p, correct_p)
    npt.assert_almost_equal(returned_t, correct_t)


def test_satlift():
    input_p = 850
    input_thetam = 20
    correct_t = 13.712979340608157
    returned_t = thermo.satlift(input_p, input_thetam)
    npt.assert_almost_equal(returned_t, correct_t)


def test_wetlift():
    input_p = 700
    input_t = 15
    input_p2 = 100
    correct_t = -81.27400812504021
    returned_t = thermo.wetlift(input_p, input_t, input_p2)
    npt.assert_almost_equal(returned_t, correct_t)


def test_lifted():
    input_p = 950
    input_t = 30
    input_td = 25
    input_lev = 100
    correct_t = -79.05621246586672
    returned_t = thermo.lifted(input_p, input_t, input_td, input_lev)
    npt.assert_almost_equal(returned_t, correct_t)














