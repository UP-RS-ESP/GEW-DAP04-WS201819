import numpy as np
from matplotlib import pyplot as pl

n = 5
m = 1000
e = 1e-8

def gendata(m):
    x = np.abs(np.random.normal(size = m))
    x[x > n-e] = n-e
    return x

bins = np.zeros(n)
data = gendata(m).astype('int')

for i in range(n):
    #bins[i] = len(data[data == i])
    bins[i] = np.sum(data == i)

pl.plot(bins)
pl.show()
pl.close('all')
