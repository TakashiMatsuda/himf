#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def mfdata(dn):
    return 0

sns.set()
mfdata = readmfdata('./experiment')
fig, ax = plt.subplots()
ax = sns.heatmap(data)
fig.savefig('param-rmse.pdf')
