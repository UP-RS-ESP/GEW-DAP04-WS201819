import numpy as np
from matplotlib import pyplot as pl

shape = (3, 5)
m = 10
xb = np.arange(shape[1]+1)
yb = np.arange(shape[0]+1)

def gendata(m, shape):
    np.random.seed(1234)
    p = np.random.random((m, 2))
    p[:, 0] *= shape[1]
    p[:, 1] *= shape[0]
    return p

bins = np.zeros(shape)
data = gendata(m, shape)
idat = data.astype('int')

for i in range(shape[0]):
    for k in range(shape[1]):
        b = (idat[:, 1] == i) * (idat[:, 0] == k)
        bins[i, k] = b.sum()

pl.pcolormesh(xb, yb, bins)
pl.colorbar()
pl.scatter(data[:, 0], data[:, 1], s = 5, c = 'r')
pl.axes().set_aspect('equal')
pl.show()
pl.close('all')
