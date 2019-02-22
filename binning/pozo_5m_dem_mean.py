import numpy as np
from matplotlib import pyplot as pl
from matplotlib.colors import LogNorm

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
ix = (0.2 * (x - x.min())).astype('int')
iy = (0.2 * (y - y.min())).astype('int')

shape = (100, 100)
xb = np.arange(x.min(), x.min()+500, 5)
yb = np.arange(y.min(), y.min()+500, 5)
mean = np.zeros(shape)
stdr = np.zeros(shape)

for i in range(shape[0]):
    print('% 3d%%' % i)
    for k in range(shape[1]):
        b = (iy == i) * (ix == k)
        mean[i, k] = z[b].mean()
        stdr[i, k] = z[b].std()

fg, ax = pl.subplots(ncols = 2,
        sharex = True, sharey = True)

im = ax[0].pcolormesh(xb, yb, mean,
        cmap = pl.cm.viridis_r)
cb = fg.colorbar(im, ax = ax[0],
        orientation = 'horizontal')
cb.set_label('Mean elevation [m]')

im = ax[1].pcolormesh(xb, yb, stdr,
        cmap = pl.cm.magma_r)
cb = fg.colorbar(im, ax = ax[1],
        orientation = 'horizontal')
cb.set_label('Elevation STD')

ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
pl.show()
