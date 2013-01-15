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








