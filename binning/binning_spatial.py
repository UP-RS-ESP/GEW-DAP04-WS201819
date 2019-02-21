import numpy as np
from matplotlib import pyplot as pl

shape = (3, 5)
m = 10
xb = np.arange(shape[1]+1)
yb = np.arange(shape[0]+1)

def gendata(m, shape):
    p = np.random.random((m, 2))
    p[:, 0] *= shape[1]
    p[:, 1] *= shape[0]
    return p

bins = np.zeros(shape)
data = gendata(m, shape)

for i in range(m):
    xi, yi = int(data[i, 0]), int(data[i, 1])
    bins[yi, xi] += 1

pl.pcolormesh(xb, yb, bins)
pl.colorbar()
pl.scatter(data[:i+1,0], data[:i+1,1], s = 5, c = 'r')
pl.axes().set_aspect('equal')
pl.show()
pl.close('all')
