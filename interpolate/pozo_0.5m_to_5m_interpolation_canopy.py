import numpy as np
from scipy.interpolate import griddata
from matplotlib import pyplot as pl

method = 'linear'
#method = 'cubic'

z2 = np.load('pozo_0.5m_dem_mean_cl2.npy')
z5 = np.load('pozo_0.5m_dem_mean_cl5.npy')
z5[np.isnan(z5)] = z2[np.isnan(z5)]

# input coords
w = 0.5
xb = np.arange(0, 500+w, w)
yb = np.arange(0, 500+w, w)
xc = xb[:-1] + w/2.
yc = yb[:-1] + w/2.
x, y = np.meshgrid(xc, yc)
x2, y2, z2 = x[~np.isnan(z2)], y[~np.isnan(z2)], z2[~np.isnan(z2)]
x5, y5, z5 = x[~np.isnan(z5)], y[~np.isnan(z5)], z5[~np.isnan(z5)]

# output coords
d = 5
Xb = np.arange(0, 500+d, d)
Yb = np.arange(0, 500+d, d)
Xc = Xb[:-1] + d/2.
Yc = Yb[:-1] + d/2.
X, Y = np.meshgrid(Xc, Yc)
Z2 = griddata((x2, y2), z2, (X, Y), method = method)
Z5 = griddata((x5, y5), z5, (X, Y), method = method)

pl.title('Canopy height [m]')
pl.pcolormesh(Xb, Xb, np.ma.masked_invalid(Z5-Z2),
        cmap = pl.cm.seismic,
        vmin = -15, vmax = 15,
        )
pl.axes().set_aspect('equal')
pl.colorbar()
pl.show()
