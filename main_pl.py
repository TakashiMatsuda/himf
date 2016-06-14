#!/Users/takashi/.pyenv/shims/python


import himf
from multiprocessing import Pool
from multiprocessing import Process
import subprocess as sbp

if __name__ == '__main__':
    cnt = 0
    himf_sbp = []
    for cnt in xrange(100):
        himf.randomizedata()
        for latentdim in xrange(1, 30, 5):
            for reg in xrange(1, 300, 50):
                cnt += 1
                if cnt > 3:
                    print "3 processes exist, waiting for the oldest process's finish..."
                    himf_sbp[0].communicate()
                    himf_sbp.pop(0)
                    cnt -= 1

                himf_sbp.append(sbp.Popen(["python", "./himf.py",
                                str(latentdim), str(reg/1000.0)]))

    for prs in himf_sbp:
        prs.communicate()
