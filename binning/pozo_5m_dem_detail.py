import sys
import numpy as np
from matplotlib import pyplot as pl

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

xr = [ck-1, ck-1, ck, ck, ck+1, ck+1, ck+2]
yr = [ci-1, ci-1, ci, ci, ci+1, ci+1, ci+2]

zx2 = [dem2[ci, j] for j in xr]
zx5 = [dem5[ci, j] for j in xr]
zy2 = [dem2[j, ck] for j in yr]
zy5 = [dem5[j, ck] for j in yr]

b2 = c == 2
b5 = c == 5

x2, y2, z2 = x[b2], y[b2], z[b2]
x5, y5, z5 = x[b5], y[b5], z[b5]

b = (iy[b2] == ci) * (ck-1 <= ix[b2]) * (ix[b2] <= ck+1)
pzx2 = z2[b]
px2 = x2[b]

b = (iy[b5] == ci) * (ck-1 <= ix[b5]) * (ix[b5] <= ck+1)
pzx5 = z5[b]
px5 = x5[b]

b = (iy[b2] <= ci+1) * (ci-1 <= iy[b2]) * (ix[b2] == ck)
pzy2 = z2[b]
py2 = y2[b]

b = (iy[b5] <= ci+1) * (ci-1 <= iy[b5]) * (ix[b5] == ck)
pzy5 = z5[b]
py5 = y5[b]

fg, ax = pl.subplots(ncols = 2, sharey = True)

ax[0].plot(xr[1:], zx2[:-1], 'm-', label = 'Class 2')
ax[0].plot(xr[1:], zx5[:-1], 'g--', label = 'Class 5')

ax[0].plot(px2, pzx2, 'r.', mfc = 'none', label = 'Class 2 points')
ax[0].plot(px5, pzx5, 'c.', mfc = 'none', label = 'Class 5 points')
ax[0].legend(loc = 'lower right')

ax[1].plot(yr[1:], zy2[:-1], 'm-', label = 'Class 2')
ax[1].plot(yr[1:], zy5[:-1], 'g--', label = 'Class 5')

ax[1].plot(py2, pzy2, 'r.', mfc = 'none', label = 'Class 2 points')
ax[1].plot(py5, pzy5, 'c.', mfc = 'none', label = 'Class 5 points')
ax[1].legend(loc = 'lower right')
pl.show()

