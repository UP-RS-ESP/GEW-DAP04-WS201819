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
    var = [[dy, dx], [100*(dy-ndy)/ndy, 100*(dx-ndx)/ndy]]
    lbl = [['dy', 'dx'], ['dy - numpy dy [%]', 'dx - numpy dx [%]']]
    levels = [np.linspace(-0.8, 0.8, 9), np.linspace(-100, 100, 6)]
    
    # create figure
    fg, ax = pl.subplots(nrows = 2, ncols = 2)
    for i in range(2):
        v = var[i]
        l = lbl[i]
        lv = levels[i]
        for k in range(2):
            im = ax[i, k].contourf(xc, yc, v[k], lv,
                    cmap = pl.cm.seismic, extend = 'both')
            im.cmap.set_under('c')
            im.cmap.set_over('m')
            cb = fg.colorbar(im, ax = ax[i, k])
            cb.set_label(l[k])
            ax[i, k].set_aspect('equal')

    pl.show()

if __name__ == '__main__':
    main()
