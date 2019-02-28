import numpy as np
from scipy.interpolate import griddata
from matplotlib import pyplot as pl

x = [1, 1, 3, 3]
y = [1, 2, 1, 2]
z = [2, 2, 4, 4]

xb = np.arange(0.5, 4, 1)
yb = np.arange(0.5, 3, 1)
xc = xb[:-1] + abs(xb[0] - xb[1]) * 0.5
yc = yb[:-1] + abs(yb[0] - yb[1]) * 0.5
print(xc, yc)

X, Y = np.meshgrid(xc, yc)

print('X:')
print(X)

print('Y:')
print(Y)

Z = griddata((x, y), z, (X, Y), method = 'linear')

print('Z:')
print(Z)

pl.pcolormesh(xb, yb, Z)
pl.colorbar()
pl.show()
