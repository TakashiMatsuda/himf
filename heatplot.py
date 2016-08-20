#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from runconfig import *

sns.set()
mfdata = np.load('avgary-{0}.npy'.format(exp_num))

fig, ax = plt.subplots()
ax = sns.heatmap(mfdata[:, 0, 0, :], cmap='bwr',
                 yticklabels=klist,
                 xticklabels=gammalist)
plt.title('RMSE By Regularization Parameter on the {0}th experiment'.format(exp_num))
plt.ylabel('K : Rank of the approximary matrix', fontsize=12)
plt.xlabel("gamma: strength of sequence regularization ", fontsize=12)
plt.yticks(rotation=0)
fig.savefig('./experiment{0}/rmseheatmap'.format(exp_num))
