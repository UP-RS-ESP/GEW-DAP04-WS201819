import sys
import numpy as np
from matplotlib import pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, z, c = pts[:, 0], pts[:, 1], pts[:, 2], pts[:, 5]
x = 0.2 * (x - x.min())
y = 0.2 * (y - y.min())
ix = x.astype('int')
iy = y.astype('int')

dem2 = np.load('pozo_5m_dem_mean_cl2.npy')
dem5 = np.load('pozo_5m_dem_mean_cl5.npy')

# fill gaps in mean
b = np.isnan(dem5)
dem5[b] = dem2[b]

ci, ck = 51, 62

b2 = c == 2
b5 = c == 5

x2, y2, z2 = x[b2], y[b2], z[b2]
x5, y5, z5 = x[b5], y[b5], z[b5]

b = (iy[b2] == ci) * (ck-1 <= ix[b2]) * (ix[b2] <= ck+1)
b += (iy[b2] <= ci+1) * (ci-1 <= iy[b2]) * (ix[b2] == ck)
px2 = x2[b]
py2 = y2[b]
pz2 = z2[b]

b = (iy[b5] == ci) * (ck-1 <= ix[b5]) * (ix[b5] <= ck+1)
b += (iy[b5] <= ci+1) * (ci-1 <= iy[b5]) * (ix[b5] == ck)
px5 = x5[b]
py5 = y5[b]
pz5 = z5[b]

fg, ax = pl.subplots(subplot_kw = dict(projection = '3d'))

ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci, ci], [ci+1, ci+1]],
                dem2[ci, ck], color = 'r', alpha = 0.5)
ax.plot_surface([[ck-1, ck], [ck-1, ck]],
                [[ci, ci], [ci+1, ci+1]],
                dem2[ci, ck-1], color = 'r', alpha = 0.5)
ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci-1, ci-1], [ci, ci]],
                dem2[ci-1, ck], color = 'r', alpha = 0.5)
ax.plot_surface([[ck+1, ck+2], [ck+1, ck+2]],
                [[ci, ci], [ci+1, ci+1]],
                dem2[ci, ck+1], color = 'r', alpha = 0.5)
ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci+1, ci+1], [ci+2, ci+2]],
                dem2[ci+1, ck], color = 'r', alpha = 0.5)

ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci, ci], [ci+1, ci+1]],
                dem5[ci, ck], color = 'c', alpha = 0.5)
ax.plot_surface([[ck-1, ck], [ck-1, ck]],
                [[ci, ci], [ci+1, ci+1]],
                dem5[ci, ck-1], color = 'c', alpha = 0.5)
ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci-1, ci-1], [ci, ci]],
                dem5[ci-1, ck], color = 'c', alpha = 0.5)
ax.plot_surface([[ck+1, ck+2], [ck+1, ck+2]],
                [[ci, ci], [ci+1, ci+1]],
                dem5[ci, ck+1], color = 'c', alpha = 0.5)
ax.plot_surface([[ck, ck+1], [ck, ck+1]],
                [[ci+1, ci+1], [ci+2, ci+2]],
                dem5[ci+1, ck], color = 'c', alpha = 0.5)

ax.scatter(px2, py2, pz2,  c = 'r', label = 'Class 2 points')
ax.scatter(px5, py5, pz5, c = 'c', label = 'Class 5 points')
ax.legend(loc = 'lower right')
pl.show()

