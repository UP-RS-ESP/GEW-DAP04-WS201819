import sys
import numpy as np
from matplotlib import pyplot as pl
from scipy.spatial.distance import pdist, squareform
from scipy.spatial import cKDTree as kdtree

def FitPlane(pnts):
    """
    Given a set of 3D points pnts.shape = (x, 3),
    return the normal vector (nx, ny, nz)
    """
    c = pnts.mean(axis = 0)
    x = pnts - c
    M = np.dot(x.T, x)
    return np.linalg.svd(M)[0][:,-1]

def main(n, r = 0.1):
    x = (np.random.random(n) - 0.5) * 4
    y = (np.random.random(n) - 0.5) * 3
    z = np.exp(-x*x-y*y)
    tree = kdtree(np.transpose((x, y)))
    slp = np.zeros(n)
    for i in range(n):
        nb = tree.query_ball_point((x[i], y[i]), r)
        pts = np.transpose((x[nb], y[nb], z[nb]))
        nx, ny, nz = FitPlane(pts)
        slp[i] = np.sqrt(nx*nx+ny*ny) / nz

    slp = np.arctan(slp) * 180 / np.pi
    pl.title('Numerical')
    pl.scatter(x, y, c = slp)
    pl.colorbar()
    pl.axes().set_aspect('equal')
    pl.show()

    # theoretical results
    rp = np.sqrt(x*x+y*y)
    sp = 2 * rp * np.exp(-rp*rp)
    sp = np.arctan(sp) * 180 / np.pi

    pl.title('Theory')
    pl.scatter(x, y, c = sp)
    pl.colorbar()
    pl.axes().set_aspect('equal')
    pl.show()

    pl.title('absolute difference')
    pl.scatter(x, y, c = slp - sp,
            cmap = pl.cm.seismic,
            vmin = -25, vmax = 25
            )
    pl.colorbar()
    pl.axes().set_aspect('equal')
    pl.show()

    pl.title('relative difference')
    pl.scatter(x, y, c = 100.*(slp - sp)/sp,
            cmap = pl.cm.seismic,
            vmin = -25, vmax = 25
            )
    pl.colorbar()
    pl.axes().set_aspect('equal')
    pl.show()

if __name__ == '__main__':
    main(200000)
