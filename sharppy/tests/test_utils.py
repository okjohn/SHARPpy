''' Frequently used functions '''
import numpy as np
import numpy.ma as ma
import numpy.testing as npt
from sharppy.sharptab.constants import MISSING, TOL
from sharppy.sharptab import utils as utils


# vec2comp Tests
def test_vec2comp_single():
    input_wdir = 225
    input_wspd = 7.0710678118654755
    correct_u = 5
    correct_v = 5
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd)
    npt.assert_almost_equal(returned_u, correct_u)
    npt.assert_almost_equal(returned_v, correct_v)

def test_vec2comp_array_like():
    input_wdir = [0, 45, 90, 135, 180, 225, 270, 315, 360]
    input_wspd = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    correct_u = [0, -7.0710678118654746, -15, -14.142135623730951, 0,
        21.213203435596423, 35, 28.284271247461909, 0]
    correct_v = [-5, -7.0710678118654746, 0, 14.142135623730951, 25,
        21.213203435596423, 0, -28.284271247461909, -45]
    correct_u = np.asanyarray(correct_u).astype(np.float64)
    correct_v = np.asanyarray(correct_v).astype(np.float64)
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd)
    npt.assert_almost_equal(returned_u, correct_u)
    npt.assert_almost_equal(returned_v, correct_v)

def test_vec2comp_zeros():
    input_wdir = [0, 90, 180, 270, 360]
    input_wspd = [10, 20, 30, 40, 50]
    correct_u = [0, -20, 0, 40, 0]
    correct_v = [-10, 0, 30, 0, -50]
    correct_u = np.asanyarray(correct_u).astype(np.float64)
    correct_v = np.asanyarray(correct_v).astype(np.float64)
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd)
    npt.assert_equal(returned_u, correct_u)
    npt.assert_equal(returned_v, correct_v)

def test_vec2comp_default_missing_val_single():
    input_wdir = MISSING
    input_wspd = 30
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd)
    npt.assert_(type(returned_u), type(ma.masked))
    npt.assert_(type(returned_v), type(ma.masked))

def test_vec2comp_default_missing_val_array():
    input_wdir = [0, 90, 180, MISSING]
    input_wspd = [MISSING, 10, 20, 30]
    correct_u = [MISSING, -10, 0, MISSING]
    correct_v= [MISSING, 0, 20, MISSING]
    correct_u = ma.asanyarray(correct_u).astype(np.float64)
    correct_v = ma.asanyarray(correct_v).astype(np.float64)
    correct_u[correct_u == MISSING] = ma.masked
    correct_v[correct_v == MISSING] = ma.masked
    correct_u[correct_v.mask] = ma.masked
    correct_v[correct_u.mask] = ma.masked
    correct_u.set_fill_value(MISSING)
    correct_v.set_fill_value(MISSING)
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd)
    npt.assert_almost_equal(returned_u, correct_u)
    npt.assert_almost_equal(returned_v, correct_v)

def test_vec2comp_user_missing_val_single():
    missing = 50
    input_wdir = missing
    input_wspd = 30
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd, missing)
    npt.assert_(type(returned_u), type(ma.masked))
    npt.assert_(type(returned_v), type(ma.masked))

def test_vec2comp_user_missing_val_array():
    missing = 50
    input_wdir = [0, 90, 180, missing]
    input_wspd = [missing, 10, 20, 30]
    correct_u = [missing, -10, 0, missing]
    correct_v= [missing, 0, 20, missing]
    correct_u = ma.asanyarray(correct_u).astype(np.float64)
    correct_v = ma.asanyarray(correct_v).astype(np.float64)
    correct_u[correct_u == missing] = ma.masked
    correct_v[correct_v == missing] = ma.masked
    correct_u[correct_v.mask] = ma.masked
    correct_v[correct_u.mask] = ma.masked
    correct_u.set_fill_value(missing)
    correct_v.set_fill_value(missing)
    returned_u, returned_v = utils.vec2comp(input_wdir, input_wspd, missing)
    npt.assert_almost_equal(returned_u, correct_u)
    npt.assert_almost_equal(returned_v, correct_v)
