#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

params = [int(x) for x in sys.argv[1:]]
sns.set()
mfdata = np.load('avgary-{0}.npy'.format(sys.argv[1]))
print(mfdata)

fig, ax = plt.subplots()
xl = [str(x/1000.0)for x in range(params[4], params[5], params[6])]
ax = sns.heatmap(mfdata, cmap='YlGnBu', vmin=1.1, vmax=1.8,
                 xticklabels=xl,
                 yticklabels=range(params[1], params[2], params[3]))
plt.title('RMSE By Parameter', fontsize=20)
plt.xlabel(u'\u03bb', fontsize=24)
plt.ylabel("k", fontsize=24)
fig.savefig('param-rmse-{0}.pdf'.format(sys.argv[1]))
