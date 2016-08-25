#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import himf
from multiprocessing import Pool
import functools
from runconfig import *

"""
probearray = val
より小さな正則化係数での実験
初期値を[-0.005, 0.005]から[-0.1, 0.1]に変更<- 難しい
maxepochsを100から1000に変更
learnrate 0.0005 -> 0.001 (x2)
earlystoppingはオフ
"""

if __name__ == '__main__':
    """
    Record experiment by copy this file
    """
    saverunconfig()

    count = 0
    for count in xrange(1):
        himf.randomizedata()
        print "{0} th test running..".format(count)
        for latentdim in klist:
            for reg in reglist:
                for nmfflag in nmflist:
                    p = Pool(1)
                    maphimf = functools.partial(himf._himf,
                                                latentdim,
                                                reg,
                                                exp_num,
                                                nmfflag=nmfflag,
                                                esflag=False,
                                                lr=lr,)
                    result = p.map(maphimf, gammalist)
                    print "result: ", result
                    p.close()
                    p.join()
