#!/Users/takashi/.pyenv/shims/python

import himf
from multiprocessing import Pool
import functools
import subprocess
import sys

exp_num = 22

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

    count = 0
    for count in xrange(100):
        himf.randomizedata()
        print "\r {0} th test running..".format(count)
        for latentdim in [1, 10, 20, 30, 40, 50]:
            for reg in [0., 0.01, 0.1, 0.5, 1]:
                for nmfflag in [False, True]:
                    p = Pool(5)
                    maphimf = functools.partial(himf._himf,
                                                latentdim,
                                                reg,
                                                exp_num,
                                                nmfflag=nmfflag,)
                    result = p.map(maphimf, [0., 0.01, 0.1, 0.5, 1])
                    print "result: ", result
                    p.close()
                    p.join()
