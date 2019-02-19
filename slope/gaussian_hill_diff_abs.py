import numpy as np
from matplotlib import pyplot as pl

shape = (7, 10)
width = 0.1
xr = np.arange(-0.5, -0.5+shape[1] * width, width)
yr = np.arange(-1.1, -1.1+shape[0] * width, width)

dem = np.zeros(shape)
for i in range(shape[0]):
    for k in range(shape[1]):
        dem[i, k] = np.exp(-yr[i]*yr[i]-xr[k]*xr[k])

dx = np.zeros(shape)
dy = np.zeros(shape)
dx[:, :-1] = (dem[:, :-1] - dem[:, 1:]) / width
dy[:-1, :] = (dem[:-1, :] - dem[1:, :]) / width

fg, ax = pl.subplots(ncols = 2)
im = ax[0].pcolormesh(xr, yr, dx, cmap = pl.cm.magma_r)
cb = fg.colorbar(im, ax = ax[0], orientation = 'horizontal')
cb.set_label('dx')
im = ax[1].pcolormesh(xr, yr, dy, cmap = pl.cm.magma_r)
cb = fg.colorbar(im, ax = ax[1], orientation = 'horizontal')
cb.set_label('dy')
ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
pl.show()
