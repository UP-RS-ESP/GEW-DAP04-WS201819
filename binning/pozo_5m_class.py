import sys
import numpy as np
from matplotlib import pyplot as pl

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, c = pts[:, 0], pts[:, 1], pts[:, 5]
ix = (0.2 * (x - x.min())).astype('int')
iy = (0.2 * (y - y.min())).astype('int')

uc, cc = np.unique(c, return_counts = True)
print(uc, cc)

shape = (100, 100)
xb = np.arange(shape[1]+1)
yb = np.arange(shape[0]+1)

fg, ax = pl.subplots(ncols = len(uc))
for i in range(len(uc)):
    print(i)
    b = c == uc[i]
    cx, cy = ix[b], iy[b]
    bins = np.zeros(shape)
    for j in range(len(cx)):
        bins[cy[j], cx[j]] += 1

    im = ax[i].pcolormesh(xb, yb, bins,
               cmap = pl.cm.magma_r,
               vmin = 0, vmax = 500
              )
    cb = fg.colorbar(im, ax = ax[i],
            orientation = 'horizontal')
    cb.set_label('Class %i with %.1e points' % (uc[i], cc[i]))
    ax[i].set_aspect('equal')

pl.show()
