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

def main(fn, m = 5000, r = 1):
    pts = np.load(fn)
    x = pts[:m,0]
    y = pts[:m,1]
    z = pts[:m,2]
    n = len(z)
    tree = kdtree(np.transpose((x, y)))
    slp = np.zeros(n)
    for i in range(n):
        nb = tree.query_ball_point((x[i], y[i]), r)
        pts = np.transpose((x[nb], y[nb], z[nb]))
        nx, ny, nz = FitPlane(pts)
        slp[i] = np.sqrt(nx*nx+ny*ny) / nz

    slp = np.arctan(slp) * 180 / np.pi

    pl.figure(1, (10.24, 7.68))
    pl.title('Pozo slope')
    pl.scatter(x, y, c = slp, s = 3,
            vmin = 0, vmax = 90)
    pl.colorbar()
    pl.axes().set_aspect('equal')
    pl.savefig('%s.png' % sys.argv[0][:-3])

if __name__ == '__main__':
    main('../pozo-steep-vegetated-pcl.npy')
