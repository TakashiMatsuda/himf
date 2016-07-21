#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
以下のパラメータ群は、今後直打を避け、キャッシュファイルへと移行されるべき物
"""
"""
exp_num = 23
klist = [10]
reglist = [0.01]
nmflist = [False, True]
gammalist = [0, 0.01, 0.1]
"""

exp_num = 26
klist = [1, 10, 20, 30, 40, 50]
reglist = [0., 0.01, 0.1, 0.5, 1]
nmflist = [False, True]
gammalist = [0., 0.01, 0.1, 0.5, 1, 2]


for k_cnt, k in enumerate(klist):
    for nmf_cnt, nmf in enumerate(nmflist):
        sns.set()
        mfdata = np.load('avgary-{0}.npy'.format(exp_num))

        fig, ax = plt.subplots()
        print "k", k, "nmf", nmf
        print mfdata[k_cnt][nmf_cnt]
        ax = sns.heatmap(mfdata[k_cnt][nmf_cnt], cmap='YlGnBu', vmin=1.4, vmax=1.6,
                         xticklabels=reglist,
                         yticklabels=gammalist)
        plt.title('RMSE By Regularization Parameter on K={0}, NMF={1}'.format(k, nmf))
        plt.xlabel(u'\u03bb', fontsize=24)
        plt.ylabel("gamma", fontsize=24)
        fig.savefig('./experiment{0}/rmseheatmap-k{1}-nmf-{2}'.format(exp_num, k, nmf))
