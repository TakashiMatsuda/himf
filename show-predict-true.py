#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
import rsvd
from runconfig_76 import *

experiment_number = sys.argv[1]

np.load('avgary-{0}.npy'.format(experiment_number), avgarray)
minimumcordinate = np.argmin(avgarray)
avgarray_shape = avgarray.shape
a = minimumcordinate // avgarray_shape[3]
a2 = minimumcordinate % avgarray_shape[3]
b = a // avgarray_shape[2]
b2 = a % avgarray_shape[2]
c = b // avgarray_shape[1]
c2 = c % avgarray_shape[1]

np.load('experiment{0}/model-ldim-{1}-reg-{2}{3}-gamma-{4}/'.format(
    experiment_number,
    klist[c],
    reglist[b2],
    "-nmf" if nmflist[c2] else "",
    gammalist[a2]))
