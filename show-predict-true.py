#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
from runconfig_76 import *

experiment_number = sys.argv[1]

avgarray = np.load('avgary-{0}.npy'.format(experiment_number))
minimumcordinate = np.argmin(avgarray)
avgarray_shape = avgarray.shape
a = minimumcordinate // avgarray_shape[3]
a2 = minimumcordinate % avgarray_shape[3]
b = a // avgarray_shape[2]
b2 = a % avgarray_shape[2]
c = b // avgarray_shape[1]
c2 = c % avgarray_shape[1]

data = np.load('experiment{0}/model-ldim-{1}-reg-{2}{3}-gamma-{4}/true_vs_prediction.npy'.format(
    experiment_number,
    klist[c],
    reglist[b2],
    "-nmf" if nmflist[c2] else "",
    gammalist[a2]))

fig, ax = plt.subplots()

plt.plot(data[:, 0], data[:, 1], 'o')
plt.show()
