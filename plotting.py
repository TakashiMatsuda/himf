#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()
mfdata = np.load('avgary-5.npy')
print(mfdata)

fig, ax = plt.subplots()
xl = [(str(x/1000.0) if x % 50 < 3 else '') for x in range(1, 300, 3)]
print xl
#cmap = sns.cubehelix_palette(as_cmap=True, light=.9)
ax = sns.heatmap(mfdata, cmap='bwr', vmin=1.3, vmax=1.8,
                 xticklabels=xl,
                 yticklabels=range(1, 36, 3))
plt.title('RMSE By Parameter', fontsize=20)
plt.xlabel(u'\u03bb', fontsize=24)
plt.ylabel("k", fontsize=24)
fig.savefig('param-rmse-5-rb.pdf')
