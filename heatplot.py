#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from runconfig import *

"""
以下のパラメータ群は、今後直打を避け、キャッシュファイルへと移行されるべき物
"""

for k_cnt, k in enumerate(klist):
    for nmf_cnt, nmf in enumerate(nmflist):
        sns.set()
        mfdata = np.load('avgary-{0}.npy'.format(exp_num))

        fig, ax = plt.subplots()
        print "k", k, "nmf", nmf
        print mfdata[k_cnt][nmf_cnt]
        ax = sns.heatmap(mfdata[k_cnt][nmf_cnt], cmap='bwr',
                         yticklabels=reglist,
                         xticklabels=gammalist)
        plt.title('RMSE By Regularization Parameter on K={0}, NMF={1}'.format(k, nmf))
        plt.ylabel(u'\u03bb'+': strength of norm regularization', fontsize=12)
        plt.xlabel("gamma: strength of sequence regularization ", fontsize=12)
        plt.yticks(rotation=0)
        fig.savefig('./experiment{0}/rmseheatmap-k{1}-nmf-{2}'.format(exp_num, k, nmf))
