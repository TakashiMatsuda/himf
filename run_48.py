#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import himf
from multiprocessing import Pool
import functools
import subprocess
import sys

exp_num = 48
"""
probearray = val
より小さな正則化係数での実験
初期値を[-0.005, 0.005]から[-0.1, 0.1]に変更<- 難しい
maxepochsを100から500に変更
learnrate 0.0005 -> 0.001 (x2)
earlystoppingはオン
"""

if __name__ == '__main__':
    """
    Record experiment by copy this file
    """
    runname = "run_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "run.py",
                                runname])
    if sc != 0:
        print "INITIALIZATION ERROR"
        sys.exit()

    klist = [50]

    reglist = [0.01]
    nmflist = [False]
    gammalist = [0., 0.00001, 0.0001]

    count = 0
    for count in xrange(5):
        himf.randomizedata()
        print "{0} th test running..".format(count)
        for latentdim in klist:
            for reg in reglist:
                for nmfflag in nmflist:
                    p = Pool(5)
                    maphimf = functools.partial(himf._himf,
                                                latentdim,
                                                reg,
                                                exp_num,
                                                nmfflag=nmfflag,)
                    result = p.map(maphimf, gammalist)
                    print "result: ", result
                    p.close()
                    p.join()
