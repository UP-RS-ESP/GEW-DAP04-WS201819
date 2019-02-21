import numpy as np
from matplotlib import pyplot as pl

m = 100000

def gendata(m):
    x = np.abs(np.random.normal(4, 3, m))
    return x

data = gendata(m)
data = data.astype('int')

counts = np.bincount(data)

pl.plot(counts)
pl.show()
