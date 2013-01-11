import numpy as np
import numpy.ma as ma
from sharppy.sharptab import constants
from sharppy.sharptab.constants import MISSING
from sharppy.sharptab.profile import Profile
import numpy.testing as npt


class TestProfile(object):
    def __init__(self):
        self.pres = [1000, 925, 850, 700, 500, 400, 300, 250, 200,
                    150, 100, 50, 30, 10]
        self.hght = [105, 769, 1487, 3099, 5750, 7400, 9430, 10660, 12090,
                    13850, 16330, 20510, 23640, MISSING]
        self.tmpc = [14.2, 15.6, 13.6, 4.8, -14.7, -25.1, -38.1, -49.1, -59.1,
                    -67.7, -64.9, -67.3, -60.7, MISSING]
        self.dwpc = [14, 15.5, 11.5, 2.2, -17.8, -30.1, -46.1, -58.1, -67.1,
                    -74.7, -73.9, -76.3, -72.7, MISSING]
        self.wdir = [95, 155, 175, 225, 235, 240, 235, 240, 235,
                    250, 235, 225, 235, MISSING]
        self.wspd = [13, 27, 24.01, 31.99, 44, 62.01, 85.01, 86, 94,
                    86, 42, 17, 42.01, MISSING]
        self.prof = Profile(pres=self.pres, hght=self.hght, tmpc=self.tmpc,
                            dwpc=self.dwpc, wdir=self.wdir, wspd=self.wspd)

    def test_prof_pres(self):
        pres = ma.asanyarray(self.pres)
        pres[pres == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.pres, pres)

    def test_prof_hght(self):
        hght = ma.asanyarray(self.hght)
        hght[hght == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.hght, hght)

    def test_prof_tmpc(self):
        tmpc = ma.asanyarray(self.tmpc)
        tmpc[tmpc == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.tmpc, tmpc)

    def test_prof_dwpc(self):
        dwpc = ma.asanyarray(self.dwpc)
        dwpc[dwpc == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.dwpc, dwpc)

    def test_prof_wdir(self):
        wdir = ma.asanyarray(self.wdir)
        wdir[wdir == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.wdir, wdir)

    def test_prof_wspd(self):
        wspd = ma.asanyarray(self.wspd)
        wspd[wspd == MISSING] = ma.masked
        npt.assert_almost_equal(self.prof.wspd, wspd)

    def test_find_sfc(self):
        correct_sfc_ind = 0
        returned_sfc_ind = self.prof.sfc
        npt.assert_equal(returned_sfc_ind, correct_sfc_ind)

    def test_find_sfc_missing_data(self):
        p = [1000, 925, 850, 700, 500, 400, 300, 250, 200]
        z = [MISSING, 769, 1487, 3099, 5750, 7400, 9430, 10660, 12090]
        t = [MISSING, 15.6, 13.6, 4.8, -14.7, -25.1, -38.1, -49.1, -59.1]
        d = [MISSING, 15.5, 11.5, 2.2, -17.8, -30.1, -46.1, -58.1, -67.1]
        wd = [MISSING, 155, 175, 225, 235, 240, 235, 240, 235]
        ws = [MISSING, 27, 24.01, 31.99, 44, 62.01, 85.01, 86, 94]
        prof = Profile(pres=p, hght=z, tmpc=t, dwpc=d, wdir=wd, wspd=ws)
        sfc_ind = 1
        npt.assert_almost_equal(prof.sfc, sfc_ind)


