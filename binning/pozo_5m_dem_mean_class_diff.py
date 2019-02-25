import sys
import numpy as np
from matplotlib import pyplot as pl

dem2 = np.load('pozo_5m_dem_mean_cl2.npy')
dem5 = np.load('pozo_5m_dem_mean_cl5.npy')

std2 = np.load('pozo_5m_dem_stdr_cl2.npy')
std5 = np.load('pozo_5m_dem_stdr_cl5.npy')

if dem2.shape[0] is not dem5.shape[0]:
    sys.exit('Y-axis do not match!')

if dem2.shape[1] is not dem5.shape[1]:
    sys.exit('X-axis do not match!')

# fill gaps in mean
b = np.isnan(dem5)
dem5[b] = dem2[b]

# fill gaps in std
b = np.isnan(std5)
std5[b] = std2[b]

shape = dem2.shape
xb = np.arange(shape[1])
yb = np.arange(shape[0])
fg, ax = pl.subplots(ncols = 2,
            sharex = True, sharey = True)
vm = np.max(dem5 - dem2)
im = ax[0].pcolormesh(xb, yb, dem5 - dem2, cmap = pl.cm.RdBu,
        vmin = -vm, vmax = vm)
cb = fg.colorbar(im, ax = ax[0], orientation = 'horizontal')
cb.set_label('Canopy height [m]')

im = ax[1].pcolormesh(xb, yb, std5 - std2)
cb = fg.colorbar(im, ax = ax[1], orientation = 'horizontal')
cb.set_label('Elevation STD difference')

ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
pl.show()

