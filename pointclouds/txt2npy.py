import sys
import numpy as np

a = np.loadtxt(sys.argv[1])
np.save('%s.npy' % sys.argv[1][:-3], a)

sys.exit()

x, y, z = np.loadtxt(sys.argv[1],
        usecols = (0, 1, 2), unpack = True)
#np.save('%s.npy' % sys.argv[1][:-3],
#        np.transpose((x, y, z)) )

np.savez('%s.npz' % sys.argv[1][:-3],
        x = x, y = y, elevation = z)
