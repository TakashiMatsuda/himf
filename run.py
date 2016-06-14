#!/Users/takashi/.pyenv/shims/python


import himf
from multiprocessing import Pool
from multiprocessing import Process
import subprocess as sbp
import sys


if __name__ == '__main__':
    print sys.argv
    params = [int(x) for x in sys.argv[1:]]
    for cnt in xrange(1, 100):
        for latentdim in xrange(params[1], params[2], params[3]):
            for reg in xrange(params[4], params[5], params[6]):
                # subprocess.call()
                    sbp.call(["python", "./himf.py", str(latentdim),
                              str(reg / 1000.0), sys.argv[1]])
