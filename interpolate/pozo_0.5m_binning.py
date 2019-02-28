import numpy as np
from matplotlib import pyplot as pl
from matplotlib.colors import LogNorm

fn = '../pozo-steep-vegetated-pcl.npy'
pts = np.load(fn)
x, y, c = pts[:, 0], pts[:, 1], pts[:, 5]
ix = (2 * (x - x.min())).astype('int')
iy = (2 * (y - y.min())).astype('int')

b = c == 5
print(len(ix))
ix, iy = ix[b], iy[b]
print(len(ix))

shape = (1000, 1000)
xb = np.arange(x.min(), x.min()+500, 0.5)
yb = np.arange(y.min(), y.min()+500, 0.5)
bins = np.zeros(shape)

for j in range(len(ix)):
    bins[iy[j], ix[j]] += 1

pl.pcolormesh(xb, yb, bins,
        cmap = pl.cm.magma_r,
        norm = LogNorm())
pl.colorbar()
pl.axes().set_aspect('equal')
pl.show()
