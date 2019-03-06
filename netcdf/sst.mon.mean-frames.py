import sys
import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as pl

n = 24

fn = 'sst.mon.mean.nc'
f = Dataset(fn, 'r')
print(f)
print(f.variables.keys())
print(f.variables['sst'])
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
sst = f.variables['sst'][:n]

lat = lat[::-1]

for i in range(n):
    pl.figure(1, (8, 6))
    pl.imshow(np.flipud(sst[i]),
            origin = 'lower',
            interpolation = 'none',
            extent = (lon[0], lon[-1],
                      lat[0], lat[-1]),
            vmin = -5, vmax = 30
            )
    pl.colorbar()
    pl.tight_layout()
    pl.savefig('%04d.png' % i)
    pl.close('all')
