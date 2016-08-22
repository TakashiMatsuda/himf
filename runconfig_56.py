#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-
import subprocess

exp_num = 56

klist = ([80, 90, 100, 110, 120])
reglist = [0., 0.002, 0.005]
nmflist = [False, True]
gammalist = [x / 10000. for x in range(5, 21)]


def saverunconfig():
    """
    Record experiment by copy this file
    """
    runname = "runconfig_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "runconfig.py",
                                runname])
