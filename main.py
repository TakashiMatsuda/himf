#!/Users/takashi/.pyenv/shims/python


import himf
from multiprocessing import Pool
from multiprocessing import Process
import subprocess as sbp


if __name__ == '__main__':
    for cnt in xrange(1, 100):
        himf.randomizedata()
        for latentdim in xrange(1, 40, 10):
            for reg in xrange(1, 300, 50):
                # TODO: make subprocess, so this area should move out of this file
                sbp.call(["python", "./himf.py", str(latentdim), str(reg/1000.0)])
