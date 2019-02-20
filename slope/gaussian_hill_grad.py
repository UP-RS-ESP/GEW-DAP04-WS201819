import numpy as np
from matplotlib import pyplot as pl

shape = (14, 20)
width = 0.15
xstart = -1.5
ystart = -1.1
xb = np.arange(xstart, xstart+(shape[1]+1) * width, width)
yb = np.arange(ystart, ystart+(shape[0]+1) * width, width)
xc = xb[:-1] + width/2
yc = yb[:-1] + width/2

X, Y = np.meshgrid(xc, yc)
dem = np.exp(-Y*Y-X*X)
dR = -2 * np.sqrt(X*X+Y*Y) * np.exp(-Y*Y-X*X)

dx = np.nan * np.ones(shape)
dy = np.nan * np.ones(shape)
dx[:, :-1] = (dem[:, 1:] - dem[:, :-1]) / width
dy[:-1, :] = (dem[1:, :] - dem[:-1, :]) / width
dx = np.ma.masked_invalid(dx)
dy = np.ma.masked_invalid(dy)
gr = np.sqrt(dx*dx+dy*dy)

fg, ax = pl.subplots(ncols = 2)

im = ax[0].pcolormesh(xb, yb, gr)
cb = fg.colorbar(im, ax = ax[0],
        orientation = 'horizontal')
cb.set_label('Gradient')
ax[0].set_aspect('equal')

im = ax[1].pcolormesh(xb, yb, dR, cmap = pl.cm.viridis_r)
cb = fg.colorbar(im, ax = ax[1],
        orientation = 'horizontal')
cb.set_label('dz / dr')
ax[1].set_aspect('equal')

pl.show()
