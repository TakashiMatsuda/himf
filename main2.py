#!/Users/takashi/.pyenv/shims/python


import himf
from multiprocessing import Pool
from multiprocessing import Process
import subprocess as sbp


if __name__ == '__main__':
    for cnt in xrange(1, 30):
        for latentdim in xrange(12, 24, 3):
            for reg in xrange(1, 300, 10):
                # TODO: make subprocess, so this area should move out of this file
                # subprocess.call()

    #                himf.himf(latentdim, reg/100.0)
                    sbp.call(["python", "./himf.py", str(latentdim), str(reg/1000.0)])
