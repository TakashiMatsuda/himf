#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()
mfdata = np.load('avgary.npy')
print(mfdata)
fig, ax = plt.subplots()
cmap = sns.cubehelix_palette(as_cmap=True, light=.9)
ax = sns.heatmap(mfdata, cmap=cmap)
fig.savefig('param-rmse.pdf')
