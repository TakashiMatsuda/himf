#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-
import subprocess

exp_num = 52

klist = range(1,30)
klist.extend([40, 45, 50, 60, 70, 80, 100])
reglist = [0.005]
nmflist = [False]
gammalist = [0., 0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01]
#gammalist = [0.0005]


def saverunconfig():
    """
    Record experiment by copy this file
    """
    runname = "runconfig_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "runconfig.py",
                                runname])
