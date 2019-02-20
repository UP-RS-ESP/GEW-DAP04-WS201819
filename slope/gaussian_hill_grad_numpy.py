import numpy as np
from matplotlib import pyplot as pl

def gradient(dem, width):
    shape = dem.shape
    dx = np.nan * np.ones(shape)
    dy = np.nan * np.ones(shape)
    dx[:, :-1] = (dem[:, 1:] - dem[:, :-1]) / width
    dy[:-1, :] = (dem[1:, :] - dem[:-1, :]) / width
    dx = np.ma.masked_invalid(dx)
    dy = np.ma.masked_invalid(dy)
    return (dy, dx)

def main():
    # define region of interest
    shape = (14, 20)
    width = 0.15
    xstart = -1.5
    ystart = -1.1
    xb = np.arange(xstart, xstart+(shape[1]+1) * width, width)
    yb = np.arange(ystart, ystart+(shape[0]+1) * width, width)
    xc = xb[:-1] + width/2
    yc = yb[:-1] + width/2
    
    # create DEM
    X, Y = np.meshgrid(xc, yc)
    dem = np.exp(-Y*Y-X*X)
    
    # numerical estimation
    dy, dx = gradient(dem, width)
    ndy, ndx = np.gradient(dem, width)
    var = [[dy, dx], [ndy, ndx]]
    lbl = [['dy', 'dx'], ['numpy dy', 'numpy dx']]
    
    # create figure
    fg, ax = pl.subplots(nrows = 2, ncols = 2)
    for i in range(2):
        v = var[i]
        l = lbl[i]
        for k in range(2):
            im = ax[i, k].pcolormesh(xb, yb, v[k])
            cb = fg.colorbar(im, ax = ax[i, k])
            cb.set_label(l[k])
            ax[i, k].set_aspect('equal')

    pl.show()

if __name__ == '__main__':
    main()
