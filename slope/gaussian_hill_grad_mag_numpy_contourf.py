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
    shape = (30, 40)
    width = 0.1
    xstart = -1.7
    ystart = -1.5
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
    dr = np.arctan(np.sqrt(dx*dx+dy*dy)) * 180 / np.pi
    ndr = np.arctan(np.sqrt(ndx*ndx+ndy*ndy)) * 180 / np.pi
    #     ^ -> degrees
    
    # create figure
    fg, ax = pl.subplots(ncols = 2)

    im = ax[0].contourf(xc, yc, ndr, 6)
    cb = fg.colorbar(im, ax = ax[0],
            orientation = 'horizontal')
    cb.set_label('Numpy gradient [deg]')
    ax[0].set_aspect('equal')

    im = ax[1].contourf(xc, yc, 100*(dr-ndr)/ndr, 10,
            cmap = pl.cm.seismic)
    cb = fg.colorbar(im, ax = ax[1],
            orientation = 'horizontal')
    cb.set_label('Rel. diff. [deg]')
    ax[1].set_aspect('equal')

    pl.show()

if __name__ == '__main__':
    main()
