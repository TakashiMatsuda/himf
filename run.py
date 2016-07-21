#!/Users/takashi/.pyenv/shims/python

import himf
from multiprocessing import Pool
from multiprocessing import Process
import functools

exp_num = 21

if __name__ == '__main__':
    count = 0
    for count in xrange(1):
        himf.randomizedata()
        print "\r {0} th test running..".format(count)
        for latentdim in [1, 10, 20, 30, 40, 50]:
            for reg in [0., 0.01, 0.1, 0.5, 1]:
                for nmfflag in [False, True]:
                    p = Pool(7)
                    maphimf = functools.partial(himf._himf,
                                                latentdim,
                                                reg,
                                                exp_num,
                                                nmfflag=nmfflag,)
                    result = p.map(maphimf, [0., 0.01, 0.1, 0.5, 1])
                    print "result: ", result
