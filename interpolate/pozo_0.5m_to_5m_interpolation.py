import numpy as np
from scipy.interpolate import griddata
from matplotlib import pyplot as pl

method = 'linear'
#method = 'cubic'

for cl in [5, 2]:
    fn = 'pozo_0.5m_dem_mean_cl%i.npy' % cl
    z = np.load(fn)

    # input coords
    w = 0.5
    xb = np.arange(0, 500+w, w)
    yb = np.arange(0, 500+w, w)
    xc = xb[:-1] + w/2.
    yc = yb[:-1] + w/2.
    x, y = np.meshgrid(xc, yc)
    x, y = x[~np.isnan(z)], y[~np.isnan(z)]
    z = z[~np.isnan(z)]

    # output coords
    d = 5
    Xb = np.arange(0, 500+d, d)
    Yb = np.arange(0, 500+d, d)
    Xc = Xb[:-1] + d/2.
    Yc = Yb[:-1] + d/2.
    X, Y = np.meshgrid(Xc, Yc)
    Z = griddata((x, y), z, (X, Y), method = method)

    # save and show
    fn = 'pozo_0.5m_to_5m_dem_%s_interp_cl%i.npy' % (method, cl)
    np.save(fn, Z)
    pl.pcolormesh(Xb, Xb, np.ma.masked_invalid(Z))
    pl.axes().set_aspect('equal')
    pl.colorbar()
    pl.show()
