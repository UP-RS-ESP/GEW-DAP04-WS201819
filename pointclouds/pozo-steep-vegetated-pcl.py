import sys
import numpy as np
from matplotlib import pyplot as pl

#fn = '%s.gz' % sys.argv[0][:-3]
#x, y, z = np.loadtxt(fn, usecols = (0, 1, 2), unpack = True)

fn = '%s.npy' % sys.argv[0][:-3]
pts = np.load(fn)
x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]

b = (150 < z) * (z < 250)
b *= (3764800 < y) * (y < 3765100)
x, y, z = x[b], y[b], z[b]

pl.scatter(x, y, s = 1, c = z)
pl.colorbar()
pl.show()
