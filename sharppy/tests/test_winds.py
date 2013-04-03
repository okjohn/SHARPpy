import numpy as np
import numpy.ma as ma
import numpy.testing as npt
import sharppy.sharptab.winds as winds
from sharppy.sharptab.profile import Profile


p = [1000., 925., 850., 700., 500., 300, 250., 200., 150., 100.]
z = [161., 798., 1496., 3086., 5720., 9370., 10570., 11970., 13700., 16230.]
t = [-9999., 1.2, 9.2, 1.6, -15.5, -43.7, -54.5, -64.1, -64.7, -58.7]
d = [-9999., 1., 9.2, -1.2, -21.5, -50.7, -62.5, -71.1, -71.7, -73.7]
wd = [-9999., 70., 175., 230., 255., 265., 255., 260., 280., 295.]
ws = [-9999., 31.99, 27.99, 25.99, 25.99, 48., 52.99, 75., 77., 39.01]
prof = Profile(pres=p, hght=z, tmpc=t, dwpc=d, wdir=wd, wspd=ws)


def test_mean_wind():
    correct = 20.103278626040353, 14.726131326109194
    returned = winds.mean_wind(prof)
    npt.assert_almost_equal(returned, correct)


def test_mean_wind():
    correct = 24.169006187866806, 12.599406561454707
    returned = winds.mean_wind_npw(prof)
    print returned
    npt.assert_almost_equal(returned, correct)