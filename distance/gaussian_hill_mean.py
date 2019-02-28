import sys
import numpy as np
from matplotlib import pyplot as pl
from distances import distances_lines as dist

def main(n, r = 0.5):
    x = (np.random.random(n) - 0.5) * 4
    y = (np.random.random(n) - 0.5) * 3
    z = np.exp(-x*x-y*y)
    D = dist(x, y)
    #i = 5
    #di = D[i, :]
    #b = di <= r
    #pl.scatter(x[b], y[b], c = 'r')
    #pl.scatter(x[~b], y[~b], c = 'b')
    #pl.scatter(x[i], y[i], c = 'c', s = 10)
    #pl.axes().set_aspect('equal')
    #pl.show()
    zavg = np.zeros(n)
    for i in range(n):
        di = D[i, :]
        b = di <= r
        zavg[i] = z[b].mean()

    pl.scatter(x, y, c = z - zavg,
            cmap = pl.cm.seismic,
            vmin = -0.1, vmax = 0.1)
    cb = pl.colorbar()
    cb.set_label('z - mean(z)')
    pl.grid()
    pl.show()

if __name__ == '__main__':
    main(1000)
