import numpy as np
import gdal, osr

def ReadGTiff(fname):
    """Reads Geo TIFF from file"""

    f = gdal.Open(fname)
    b = f.GetRasterBand(1)
    a = b.ReadAsArray()
    m = b.GetNoDataValue()
    a[a == m] = np.nan
    return a

def WriteGTiff(fname, arr, xmin, ymax, step):
    drv = gdal.GetDriverByName('GTiff')
    out = drv.Create(fname, arr.shape[1], arr.shape[0], 1, 6)
    out.SetGeoTransform((xmin, step, 0, ymax, 0, -step))
    bnd = out.GetRasterBand(1)
    bnd.WriteArray(arr)
    ref = osr.SpatialReference()
    ref.ImportFromEPSG(26911)
    out.SetProjection(ref.ExportToWkt())
    bnd.SetNoDataValue(np.nan)
    bnd.FlushCache()
    del ref, bnd, out, drv

