import numpy as np
from matplotlib import pyplot as pl
from time import time

shape = (100, 100)
m = 10 * shape[0] * shape[1]
xb = np.arange(shape[1]+1)
yb = np.arange(shape[0]+1)

def gendata(m, shape):
    p = np.random.random((m, 2))
    p[:, 0] *= shape[1]
    p[:, 1] *= shape[0]
    return p

bins = np.zeros(shape)
binz = np.zeros(shape)
data = gendata(m, shape)
idat = data.astype('int')

t0 = time()
for i in range(shape[0]):
    for k in range(shape[1]):
        b = (idat[:, 1] == i) * (idat[:, 0] == k)
        bins[i, k] = b.sum()

t1 = time()
print(t1 - t0)
t0 = time()
for j in range(m):
    i, k = idat[j, 1], idat[j, 0]
    binz[i, k] += 1

t1 = time()
print(t1 - t0)

pl.pcolormesh(xb, yb, bins - binz, cmap = pl.cm.seismic)
pl.colorbar()
pl.axes().set_aspect('equal')
pl.tight_layout()
pl.show()
pl.close('all')
