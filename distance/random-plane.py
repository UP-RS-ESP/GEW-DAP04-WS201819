import numpy as np
from matplotlib import pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

def FitPlane(pnts):
    """
    Given a set of 3D points pnts.shape = (x, 3),
    return the normal vector (nx, ny, nz)
    """
    c = pnts.mean(axis = 0)
    x = pnts - c
    M = np.dot(x.T, x)
    return np.linalg.svd(M)[0][:,-1]

# random point cloud neighborhood
n = 123
x = np.random.normal(size = n)
y = np.random.normal(size = n)
z = x + np.random.random(n)

# plane fit
points = np.transpose((x, y, z))
normal = FitPlane(points)

# construct a plane plotable by matplotlib
xr = np.linspace(x.min(), x.max())
yr = np.linspace(y.min(), y.max())
xx, yy = np.meshgrid(xr, yr)
centroid = points.mean(axis = 0)
zz = (centroid.dot(normal) - normal[0] * xx - normal[1] * yy) / normal[2]

# 3D figure
fg, ax = pl.subplots(subplot_kw = dict(projection = '3d'))
ax.plot_surface(xx, yy, zz, alpha = 0.2)
ax.scatter(x, y, z,  color = 'r')
pl.show()
