#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns


def readvsdata():
    return 0


sns.set()
vsdata = readvsdata()
fig, ax = plt.subplots()
ax = sns.regplot(vsdata[0], vsdata[1])
fig.savefig('bestparam-res.pdf')
