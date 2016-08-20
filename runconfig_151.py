#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-
import subprocess

exp_num = 151

#klist = range(1, 100)
klist = [100]
#reglist = [x / 1000. for x in xrange(0, 200)]
reglist = [0.0001]
#nmflist = [False, True]
nmflist = [True]
#gammalist = [0., 0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01]
gammalist = [0.0005]


def saverunconfig():
    """
    Record experiment by copy this file
    """
    runname = "runconfig_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "runconfig.py",
                                runname])
