#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-
import subprocess

exp_num = 94
"""
離散している値を取っているデータ集合に対する性能評価の実験
"""

klist = [10, 20, 25, 30, 40, 50, 100]
reglist = [0.005]
nmflist = [False]
gammalist = [0, 0.0001, 0.001]
lr = 0.005


def saverunconfig():
    """
    Record experiment by copy this file
    """
    runname = "runconfig_{0}.py".format(exp_num)
    sc = subprocess.check_call(["cp",
                                "runconfig.py",
                                runname])
