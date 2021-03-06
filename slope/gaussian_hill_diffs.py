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
tdx = -2 * X * np.exp(-Y*Y-X*X)
tdy = -2 * Y * np.exp(-Y*Y-X*X)

dx = np.nan * np.ones(shape)
dy = np.nan * np.ones(shape)
dx[:, :-1] = (dem[:, 1:] - dem[:, :-1]) / width
dy[:-1, :] = (dem[1:, :] - dem[:-1, :]) / width
dx = np.ma.masked_invalid(dx)
dy = np.ma.masked_invalid(dy)

fg, ax = pl.subplots(ncols = 2, nrows = 2)
var = [[tdx, tdy], [dx, dy]]
lbl = [['tdx', 'tdy'], ['dx', 'dy']]

for i in range(2):
    v = var[i]
    l = lbl[i]
    for k in range(2):
        im = ax[i, k].pcolormesh(xb, yb, v[k])
        cb = fg.colorbar(im, ax = ax[i, k])
        cb.set_label(l[k])
        ax[i, k].set_aspect('equal')

pl.show()
