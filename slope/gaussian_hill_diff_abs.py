import numpy as np
from matplotlib import pyplot as pl

shape = (7, 10)
width = 0.1
xb = np.arange(-0.5, -0.5+(shape[1]+1) * width, width)
yb = np.arange(-1.1, -1.1+(shape[0]+1) * width, width)
xc = xb[:-1] + width/2
yc = yb[:-1] + width/2
X, Y = np.meshgrid(xc, yc)
dem = np.exp(-Y*Y-X*X)
tdx = -2 * X * np.exp(-Y*Y-X*X)
tdy = -2 * Y * np.exp(-Y*Y-X*X)

dx = np.nan * np.ones(shape)
dy = np.nan * np.ones(shape)
dx[:, :-1] = (dem[:, :-1] - dem[:, 1:]) / width
dy[:-1, :] = (dem[:-1, :] - dem[1:, :]) / width
dx = np.ma.masked_invalid(dx)
dy = np.ma.masked_invalid(dy)

fg, ax = pl.subplots(ncols = 2)
im = ax[0].pcolormesh(xb, yb, dx-tdx,
        cmap = pl.cm.seismic, vmin = -1.7, vmax = 1.7)
cb = fg.colorbar(im, ax = ax[0], orientation = 'horizontal')
cb.set_label('absolute dx deviation')
im = ax[1].pcolormesh(xb, yb, dy-tdy,
        cmap = pl.cm.seismic, vmin = -1.7, vmax = 1.7)
cb = fg.colorbar(im, ax = ax[1], orientation = 'horizontal')
cb.set_label('absolute dy deviation')
ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
pl.show()
