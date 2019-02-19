import sys
import numpy as np
from matplotlib import pyplot as pl

n = 100
sfr = np.logspace(0, 1, n)
tfl = np.zeros(n)

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
    
    fg, ax = pl.subplots(ncols = 2, nrows = 2,
            figsize = (10.24, 7.68))
    var = [[tdx, tdy], [dx-tdx, dy-tdy]]
    lbl = [['tdx', 'tdy'], ['absolute dx deviation', 'absolute dy deviation']]
    
    i = 0
    v = var[i]
    l = lbl[i]
    for k in range(2):
        im = ax[i, k].pcolormesh(xb, yb, v[k])
        cb = fg.colorbar(im, ax = ax[i, k])
        cb.set_label(l[k])
        ax[i, k].set_xlim((xstart, 2.2))
        ax[i, k].set_ylim((ystart, -ystart))
        ax[i, k].set_aspect('equal')
    
    i = 1
    v = var[i]
    l = lbl[i]
    for k in range(2):
        im = ax[i, k].pcolormesh(xb, yb, v[k],
                cmap = pl.cm.seismic, vmin = -0.2, vmax = 0.2)
        cb = fg.colorbar(im, ax = ax[i, k])
        cb.set_label(l[k])
        ax[i, k].set_xlim((xstart, 2.2))
        ax[i, k].set_ylim((ystart, -ystart))
        ax[i, k].set_aspect('equal')

    fn = 'foo-%04d.png' % j
    print(fn)
    pl.savefig(fn)
    pl.close('all')
