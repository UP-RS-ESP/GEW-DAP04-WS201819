import sys
import numpy as np
from laspy.file import File

fname = sys.argv[1]
f = File(fname, mode = 'r')
x = f.x
y = f.y
z = f.z

