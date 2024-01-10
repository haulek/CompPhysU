#!/usr/bin/env python3

print('Hello world')
import imanc  # We now import pybind11 module, produced with C++ code
from numpy import *
import time
import matplotlib.cm as cm
from matplotlib.pylab import *

data3 = ones((1000,1000))

t0 = time.time()
imanc.mand(data3, 1000, 1000, 1000, [-2,1,-1,1])
t1 = time.time()

print('pybind11: walltime: ', t1-t0)


imshow(-log(data3), extent=[-2,1,-1,1], cmap=cm.hot)  
show()
