import numpy as np
from matplotlib import pyplot as pl
from matplotlib.colors import LogNorm

#fn = '../pozo-steep-vegetated-pcl.npy'
#pts = np.load(fn)
#x, y = pts[:, 0], pts[:, 1]
fn = '../pozo-steep-vegetated-pcl.npz'
f = np.load(fn)
x = f['x']
y = f['y']
f.close()

ix = (0.2 * (x - x.min())).astype('int')
iy = (0.2 * (y - y.min())).astype('int')

shape = (100, 100)
#xb = np.arange(shape[1]+1)
#yb = np.arange(shape[0]+1)
xb = np.arange(x.min(), x.min()+500, 5)
yb = np.arange(y.min(), y.min()+500, 5)
bins = np.zeros(shape)

for j in range(len(ix)):
    bins[iy[j], ix[j]] += 1

cmap = pl.cm.magma_r
norm = LogNorm()
pl.pcolormesh(xb, yb, bins,
        cmap = cmap,
        #norm = norm,
        )
pl.colorbar()
pl.axes().set_aspect('equal')
pl.show()
