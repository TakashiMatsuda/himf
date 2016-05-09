#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()
mfdata = np.load('avgary-3.npy')
print(mfdata)

fig, ax = plt.subplots()
#cmap = sns.cubehelix_palette(as_cmap=True, light=.9)
ax = sns.heatmap(mfdata, cmap='bwr', vmin=1.3, vmax=1.8)
fig.savefig('param-rmse-3-rb.pdf')
