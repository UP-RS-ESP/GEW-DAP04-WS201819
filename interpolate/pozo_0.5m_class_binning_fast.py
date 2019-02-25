import sys
import numpy as np
from matplotlib import pyplot as pl

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, z, c = pts[:, 0], pts[:, 1], pts[:, 2], pts[:, 5]
ix = (2 * (x - x.min())).astype('int')
iy = (2 * (y - y.min())).astype('int')

shape = (1000, 1000)
xb = np.arange(shape[1])
yb = np.arange(shape[0])
fg, ax = pl.subplots(ncols = 2,
            #figsize = (10.24, 7.68),
            sharex = True, sharey = True)

uc = (2, 5)
for j in range(len(uc)):
    print('Class %i' % uc[j])
    b = c == uc[j]
    cx, cy, cz = ix[b], iy[b], z[b]

    mean = np.zeros(shape)
    bins = np.zeros(shape)
    for k in range(len(cz)):
        mean[cy[k], cx[k]] += cz[k]
        bins[cy[k], cx[k]] += 1

    mean /= bins
    mean[bins == 0] = np.nan
    np.save('pozo_0.5m_dem_mean_cl%i_onepass.npy' % uc[j], mean)
    ax[j].set_title('Class %i' % uc[j])
    im = ax[j].pcolormesh(xb, yb,
                  np.ma.masked_invalid(mean),
                  cmap = pl.cm.viridis_r)
    cb = fg.colorbar(im, ax = ax[j])
    cb.set_label('Mean elevation [m]')
    ax[j].set_aspect('equal')

pl.savefig('%s.png' % sys.argv[0][:-3])
