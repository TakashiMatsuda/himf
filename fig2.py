#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()
vsdata = np.load('bestparam-res.npy')
print vsdata
xlist = []
ylist = []
for i, elem in enumerate(vsdata):
    xlist.append(vsdata[i][0])
    ylist.append(vsdata[i][1])
fig, ax = plt.subplots()
x, y = vsdata.T
ax = sns.regplot(x=x, y=y)
fig.savefig('bestparam-plot.pdf')
