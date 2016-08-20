#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-
import subprocess

exp_num = 53

klist = ([100, 120, 150, 200])
reglist = [0.005]
nmflist = [False]
gammalist = [0., 0.00001, 0.0005, 0.001, 0.003, 0.005]


def saverunconfig():
    """
    Record experiment by copy this file
    """
    runname = "runconfig_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "runconfig.py",
                                runname])
