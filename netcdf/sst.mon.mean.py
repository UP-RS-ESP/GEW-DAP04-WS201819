import sys
import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as pl

fn = '%s.nc' % sys.argv[0][:-3]
f = Dataset(fn, 'r')
print(f)
print(f.variables.keys())
print(f.variables['sst'])
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
sst = f.variables['sst'][:]

# long term average
sst = sst.mean(axis = 0)
sst = np.flipud(sst)
lat = lat[::-1]

pl.imshow(sst,
        origin = 'lower',
        interpolation = 'none',
        extent = (lon[0], lon[-1],
                  lat[0], lat[-1]),
        )
pl.colorbar()
pl.tight_layout()
pl.show()
