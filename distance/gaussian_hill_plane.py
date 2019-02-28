import sys
import numpy as np
from matplotlib import pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from distances import distances_lines as dist

def Surface(normal, pts):
    xr = np.linspace(pts[:,0].min(), pts[:,0].max())
    yr = np.linspace(pts[:,1].min(), pts[:,1].max())
    xx, yy = np.meshgrid(xr, yr)
    centroid = pts.mean(axis = 0)
    zz = (centroid.dot(normal) - normal[0] * xx - normal[1] * yy) / normal[2]
    return (xx, yy, zz)

def FitPlane(pnts):
    """
    Given a set of 3D points pnts.shape = (x, 3),
    return the normal vector (nx, ny, nz)
    """
    c = pnts.mean(axis = 0)
    x = pnts - c
    M = np.dot(x.T, x)
    return np.linalg.svd(M)[0][:,-1]

def main(n, r = 0.3):
    x = (np.random.random(n) - 0.5) * 4
    y = (np.random.random(n) - 0.5) * 3
    z = np.exp(-x*x-y*y)
    D = dist(x, y)
    i = 5
    di = D[i, :]
    b = di <= r
    pts = np.transpose((x[b], y[b], z[b]))
    normal = FitPlane(pts)
    nx, ny, nz = normal
    nr = np.sqrt(nx*nx+ny*ny)
    print(nx, ny, nz, nr/nz)

    xx, yy, zz = Surface(normal, pts)
    fg, ax = pl.subplots(subplot_kw = dict(projection = '3d'))
    ax.plot_surface(xx, yy, zz, alpha = 0.2)
    ax.scatter(x[b], y[b], z[b], s = 5, color = 'r')
    ax.scatter(x[~b], y[~b], z[~b], s = 1, color = 'c')
    pl.show()

if __name__ == '__main__':
    main(1000)
