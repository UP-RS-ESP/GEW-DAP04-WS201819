import sys
import numpy as np
from matplotlib import pyplot as pl

def distances_triangle(x, y):
    n = len(x)
    D = np.zeros((n, n))
    for i in range(n):
        xi, yi = x[i], y[i]
        for k in range(i):
            dx = xi - x[k]
            dy = yi - y[k]
            D[i, k] = D[k, i] = dx*dx+dy*dy

    return np.sqrt(D)

def distances_lines(x, y):
    n = len(x)
    D = np.zeros((n, n))
    for i in range(n):
        dx = x[i] - x
        dy = y[i] - y
        D[i, :] = dx*dx+dy*dy

    return np.sqrt(D)

def main(n):
    from time import time

    x = (np.random.random(n) - 0.5) * 4
    y = (np.random.random(n) - 0.5) * 3
    z = np.exp(-x*x-y*y)

    #nodes = np.arange(n)
    #i = np.argsort(x)
    #x, y, z = x[i], y[i], z[i]

    t0 = time()
    D = distances_lines(x, y)
    t1 = time()
    #print(D)

    t2 = time()
    D = distances_triangle(x, y)
    t3 = time()
    #print(D)

    return (t1-t0, t3-t2)

if __name__ == '__main__':
    nr = [10, 50, 100, 500, 1000, 5000]
    #nr = [4, 5]
    tls = np.zeros(len(nr))
    ttr = np.zeros(len(nr))

    for i in range(len(nr)):
        n = nr[i]
        tls[i], ttr[i] = main(n)

    pl.loglog(nr, tls, label = 'distance by lines')
    pl.loglog(nr, ttr, label = 'distance by triangle')
    pl.legend()
    pl.xlabel('number of points')
    pl.ylabel('run time [sec]')
    pl.show()
