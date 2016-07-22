#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import numpy as np

exp_num = 29
klist = [1, 10, 20, 30, 40, 50]
reglist = [0., 0.01, 0.1, 0.5, 1]
nmflist = [False, True]
gammalist = [0., 0.01, 0.1, 0.5, 1]

mn_mf = 100.
mn_nmf = 100.
mn_mf_align = 100.
mn_nmf_align = 100.
mnparam_mf = [0. for x in xrange(2)]
mnparam_nmf = [0. for x in xrange(2)]
mnparam_mf_align = [0. for x in xrange(3)]
mnparam_mf_align = [0. for x in xrange(3)]


avgarray = np.load("avgary-{0}.npy".format(exp_num))


# mf

        # nmf
        # mf_align
        # nmf_align
