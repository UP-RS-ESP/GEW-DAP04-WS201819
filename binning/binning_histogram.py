import numpy as np
from matplotlib import pyplot as pl

m = 100000

def gendata(m):
    x = np.abs(np.random.normal(4, 3, m))
    return x

data = gendata(m)
idata = data.astype('int')

counts = np.bincount(idata)
nbins = counts.shape[0]
hist, edges = np.histogram(data, bins = np.arange(nbins+1))

pl.plot(counts, label = 'bincount')
pl.plot(hist, label = 'histogram')
pl.legend(loc = 'lower left')
pl.show()
