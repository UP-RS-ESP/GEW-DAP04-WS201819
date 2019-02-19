import numpy as np
from matplotlib import pyplot as pl
#import matplotlib.pyplot as pl
#from matplotlib.colors import LogNorm

shape = (7, 10)
xr = np.arange(-0.5, -0.5+shape[1]*0.2, 0.2)
yr = np.arange(-1.1, -1.1+shape[0]*0.2, 0.2)

dem = np.zeros(shape)
for i in range(shape[0]):
    for k in range(shape[1]):
        dem[i, k] = np.exp(-yr[i]*yr[i]-xr[k]*xr[k])

#pl.pcolormesh(xr, yr, dem, cmap = pl.cm.magma, norm = LogNorm())
pl.pcolormesh(xr, yr, dem, cmap = pl.cm.magma_r)
pl.xlabel('X')
pl.ylabel('Y')
cb = pl.colorbar()
cb.set_label('Z')
pl.show()
