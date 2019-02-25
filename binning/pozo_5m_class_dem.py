import sys
import numpy as np
from matplotlib import pyplot as pl
from rw import WriteGTiff

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, z, c = pts[:, 0], pts[:, 1], pts[:, 2], pts[:, 5]
ix = (0.2 * (x - x.min())).astype('int')
iy = (0.2 * (y - y.min())).astype('int')

shape = (100, 100)
xb = np.arange(shape[1])
yb = np.arange(shape[0])
fg, ax = pl.subplots(ncols = 2, nrows = 2,
            figsize = (10.24, 10.24),
            sharex = True, sharey = True)

uc = (2, 5)
for j in range(len(uc)):
    print('Class %i' % uc[j])
    b = c == uc[j]
    cx, cy, cz = ix[b], iy[b], z[b]

    mean = np.zeros(shape)
    stdr = np.zeros(shape)
    for i in range(shape[0]):
        print('% 3d%%' % i)
        for k in range(shape[1]):
            b = (cy == i) * (cx == k)
            mean[i, k] = cz[b].mean()
            stdr[i, k] = cz[b].std()

    fname = 'pozo_5m_dem_mean_cl%i.tif' % uc[j]
    WriteGTiff(fname, mean, x.min(), y.min()+500, step = 5)
    np.save('pozo_5m_dem_mean_cl%i.npy' % uc[j], mean)
    np.save('pozo_5m_dem_stdr_cl%i.npy' % uc[j], stdr)
    ax[0, j].set_title('Class %i' % uc[j])
    im = ax[0, j].pcolormesh(xb, yb,
                  np.ma.masked_invalid(mean),
                  cmap = pl.cm.viridis_r)
    cb = fg.colorbar(im, ax = ax[0, j])
    cb.set_label('Mean elevation [m]')

    im = ax[1, j].pcolormesh(xb, yb,
                  np.ma.masked_invalid(stdr),
                  cmap = pl.cm.magma_r)
    cb = fg.colorbar(im, ax = ax[1, j])
    cb.set_label('Elevation STD')
    ax[0, j].set_aspect('equal')
    ax[1, j].set_aspect('equal')

pl.savefig('%s.png' % sys.argv[0][:-3])
