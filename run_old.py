#!/Users/takashi/.pyenv/shims/python

import subprocess as sbp
import sys

if __name__ == '__main__':
    print sys.argv
    params = [int(x) for x in sys.argv[1:]]
    for cnt in xrange(1, 100):
#        for latentdim in xrange(params[1], params[2], params[3]):
        for latentdim in [1, 10, 20, 30, 40, 50]:
#            for reg in xrange(params[4], params[5], params[6]):
            for reg in [0., 0.01, 0.1, 0.5, 1]:
                for gamma in [0., 0.01, 0.1, 0.5, 1]:
                # subprocess.call()
                    sbp.call(["python", "./himf.py", str(latentdim),
                              str(reg / 1000.0), sys.argv[1]])
