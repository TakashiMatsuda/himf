#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()
mfdata = np.load('avgary-3.npy')
print(mfdata)
print mfdata[7][50]
fig, ax = plt.subplots()
#cmap = sns.cubehelix_palette(as_cmap=True, light=.9)
ax = sns.heatmap(mfdata, cmap='YlGnBu', vmin=1.3, vmax=1.8)
fig.savefig('param-rmse-3.pdf')
