import numpy as np
import numpy.ma as ma
import numpy.testing as npt
import sharppy.sharptab.winds as winds
import sharppy.sharptab.utils as utils
import sharppy.sharptab.interp as interp
import sharppy.sharptab.thermo as thermo
from sharppy.sharptab.profile import Profile
import sharppy.sharptab.params as params
import test_profile


prof = test_profile.TestProfile().prof
prof2 = test_profile.prof2


# def test_k_index():
#     correct = 29.
#     returned = params.k_index(prof)
#     npt.assert_almost_equal(returned, correct)


# def test_c_totals():
#     correct = 27.4
#     returned = params.c_totals(prof)
#     npt.assert_almost_equal(returned, correct)


# def test_v_totals():
#     correct = 28.5
#     returned = params.v_totals(prof)
#     npt.assert_almost_equal(returned, correct)


# def test_t_totals():
#     correct = 55.9
#     returned = params.t_totals(prof)
#     npt.assert_almost_equal(returned, correct)


# def test_precip_water():
#     correct = 1.0764334872877548
#     returned = params.precip_water(prof, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 1.0754792817682868
#     returned = params.precip_water(prof, exact=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 1.076869948721991
#     returned = params.precip_water(prof2, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 1.0759180707182694
#     returned = params.precip_water(prof2, exact=False)
#     npt.assert_almost_equal(returned, correct)


# def test_temp_lvl():
#     correct = 202.
#     returned = params.temp_lvl(prof, -65.90)
#     npt.assert_almost_equal(returned, correct)

#     correct = 818.7
#     returned = params.temp_lvl(prof, 9.01)
#     npt.assert_almost_equal(returned, correct)

#     correct = ma.masked
#     returned = params.temp_lvl(prof, 100)
#     npt.assert_(type(returned), type(correct))

#     correct = 667.215031955
#     returned = params.temp_lvl(prof, 0)
#     npt.assert_almost_equal(returned, correct)

#     correct = 233.217896871
#     returned = params.temp_lvl(prof, -60)
#     npt.assert_almost_equal(returned, correct)

#     correct = ma.masked
#     returned = params.temp_lvl(prof, -100)
#     npt.assert_(type(returned), type(correct))


# def test_max_temp():
#     correct = 23.48059514803731
#     returned = params.max_temp(prof)
#     npt.assert_almost_equal(returned, correct)


# def test_mean_mixratio():
#     correct = 9.9097126698366704
#     returned = params.mean_mixratio(prof, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 9.8305848290789228
#     returned = params.mean_mixratio(prof, exact=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 9.9390072423328757
#     returned = params.mean_mixratio(prof2, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 9.8415428124417623
#     returned = params.mean_mixratio(prof2, exact=False)
#     npt.assert_almost_equal(returned, correct)


# def test_mean_theta():
#     correct = 23.860993571020618
#     returned = params.mean_theta(prof, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 23.444679481624146
#     returned = params.mean_theta(prof, exact=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 23.928963700357173
#     returned = params.mean_theta(prof2, exact=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 23.4491403689
#     returned = params.mean_theta(prof2, exact=False)
#     npt.assert_almost_equal(returned, correct)


# def test_lapse_rate():
#     correct = 7.51423785435
#     returned = params.lapse_rate(prof, 0, 3000, pres=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 8.0593831522471451
#     returned = params.lapse_rate(prof, 3000, 6000, pres=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 7.078778368123635
#     returned = params.lapse_rate(prof, 850., 500., pres=True)
#     npt.assert_almost_equal(returned, correct)

#     correct = 8.147353260838399
#     returned = params.lapse_rate(prof, 700., 500., pres=True)
#     npt.assert_almost_equal(returned, correct)


# def test_most_unstable_layer():
#     correct = 976.0
#     returned = params.most_unstable_level(prof, exact=False)
#     npt.assert_almost_equal(returned, correct)

#     correct = 976.0
#     returned = params.most_unstable_level(prof, exact=True)
#     npt.assert_almost_equal(returned, correct)


# # def test_parcelx():
# #     pcl1 = params.parcelx(prof, flag=6)
# #     for prop, value in vars(pcl1).iteritems():
# #         if prop == 'lplvals':
# #             print 'lplvals.desc: ', value.desc
# #             print 'lplvals.pres: ', value.pres
# #             print 'lplvals.tmpc: ', value.tmpc
# #             print 'lplvals.dwpc: ', value.dwpc
# #         else:
# #             print prop, ": ", value

# #     # pcl2 = params.parcelx(prof, flag=2)
# #     # pcl3 = params.parcelx(prof, flag=3)
# #     # pcl4 = params.parcelx(prof, flag=4)

# #     # pcl11 = params.parcelx(prof2, flag=1)
# #     # pcl22 = params.parcelx(prof2, flag=2)
# #     # pcl33 = params.parcelx(prof2, flag=3)
# #     # pcl44 = params.parcelx(prof2, flag=4)

# #     # print pcl1.bplus, pcl2.bplus, pcl3.bplus, pcl4.bplus
# #     # print pcl11.bplus, pcl22.bplus, pcl33.bplus, pcl44.bplus


# def test_effective_inflow_layer():
#     mupcl = params.parcelx(prof, flag=3)
#     params.effective_inflow_layer(prof, mupcl=mupcl)

#     params.effective_inflow_layer(prof)

#     prof.mupcl = mupcl
#     params.effective_inflow_layer(prof)


def test_convective_temp():
    correct = 73.76
    returned = params.convective_temp(prof)
    npt.assert_almost_equal(returned, correct)
