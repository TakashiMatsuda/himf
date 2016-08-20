#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import numpy as np
from runconfig import *

nmf_loop_list = ["-nmf" if x else "" for x in nmflist]

mn = 100.
mnparam = [0 for x in xrange(4)]
avgarray = np.zeros((len(klist), len(nmflist), len(reglist), len(gammalist)))

for ldim_cnt, ldim in enumerate(klist):
    for nmf_cnt, nmf in enumerate(nmf_loop_list):
        for reg_cnt, reg in enumerate(reglist):
            for gamma_cnt, gamma in enumerate(gammalist):
                cnt = 0
                s = 0.
                f = open('./experiment{0}/rmse-ldim-{1}-reg-{2}{3}-gamma-{4}'.format(exp_num, ldim, reg, nmf, gamma))
                for line in f:
                    cnt = cnt + 1
                    s = s + float(line.split()[2])
                avg = s / cnt

                if avg < mn:
                    mn = avg
                    mnparam[0] = ldim
                    mnparam[1] = reg
                    mnparam[2] = nmf
                    mnparam[3] = gamma

                f.close()
                avgarray[ldim_cnt][nmf_cnt][reg_cnt][gamma_cnt] = avg
                print avg

"""
nmfごと、gamma0とそれ以外のbestparameterが必要
bestparameterをとるのは別のスクリプトに分離して実装してください
"""

np.save('avgary-{0}.npy'.format(exp_num), avgarray)
#np.save('bestparam-{0}-{1}.npy'.format(exp_num, ))
