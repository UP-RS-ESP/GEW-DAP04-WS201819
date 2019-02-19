import sys
import numpy as np
from matplotlib import pyplot as pl
from time import time

n = 20
sfr = np.logspace(0, 2, n)
tfor = np.zeros(n)
tvec = np.zeros(n)

for j in range(len(sfr)):
    sf = sfr[j]
    shape = (int(sf * 15), int(sf * 20))
    width = 0.2 / sf
    xstart = -1.7
    ystart = -1.5
    xb = np.arange(xstart, xstart+(shape[1]+1) * width, width)
    yb = np.arange(ystart, ystart+(shape[0]+1) * width, width)
    xb = xb[:shape[1]+1]
    yb = yb[:shape[0]+1]
    xc = xb[:-1] + width/2
    yc = yb[:-1] + width/2
    t0 = time()
    X, Y = np.meshgrid(xc, yc)
    dem = np.exp(-Y*Y-X*X)
    t1 = time()
    #tdx = -2 * X * np.exp(-Y*Y-X*X)
    #tdy = -2 * Y * np.exp(-Y*Y-X*X)
    dem = np.zeros(shape)
    #tdx = np.zeros(shape)
    #tdy = np.zeros(shape)
    for i in range(shape[0]):
        for k in range(shape[1]):
            r2 = yc[i]*yc[i]+xc[k]*xc[k]
            dem[i, k] = np.exp(-r2)
            #tdx[i, k] = -2 * xc[k] * np.exp(-r2)
            #tdy[i, k] = -2 * yc[i] * np.exp(-r2)
    t2 = time()
    tvec[j] = t1 - t0
    tfor[j] = t2 - t1

pl.figure(1, (10.24, 7.68))
pl.loglog(sfr, tvec, 'ro-', mfc = 'none', label = 'vectorized')
pl.loglog(sfr, tfor, label = 'for loops')
pl.xlabel('Spatial scale')
pl.ylabel('Run time [s]')
pl.legend(loc = 'upper left')
pl.show()

