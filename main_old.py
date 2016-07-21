#!/Users/takashi/.pyenv/shims/python


import himf
from multiprocessing import Pool
from multiprocessing import Process
import subprocess as sbp

if __name__ == '__main__':
    cnt = 0
    himf_sbp = []
    for count in xrange(100):
        himf.randomizedata()
        print "\r {0} th test running..".format(count)
        for latentdim in [1, 10, 20, 30, 40, 50]:
#            for reg in xrange(params[4], params[5], params[6]):
            for reg in [0., 0.01, 0.1, 0.5, 1]:
                for gamma in [0., 0.01, 0.1, 0.5, 1]:
                    cnt += 1
                    if cnt > 3:
                        print "3 processes exist, waiting for the oldest process's finish..."
                        himf_sbp[0].communicate()
                        himf_sbp.pop(0)
                        cnt -= 1

                himf_sbp.append(sbp.Popen(["python", "./himf.py",
                                str(latentdim), str(reg), str()]))

    for prs in himf_sbp:
        prs.communicate()
