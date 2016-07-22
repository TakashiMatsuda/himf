#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import himf
from multiprocessing import Pool
import functools
import subprocess
import sys

exp_num = 30
"""
probearray = val
配列による正則化のはんか性能を確認するための実験
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

    klist = [1, 10, 20, 30, 40]

    reglist = [0., 0.01, 0.1, 0.5, 1]
    nmflist = [False, True]
    gammalist = [0., 0.01, 0.1, 0.5, 1]

    count = 0
    for count in xrange(50):
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
