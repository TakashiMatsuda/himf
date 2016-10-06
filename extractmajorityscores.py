#!/Users/takashi/.pyenv/shims/python

import numpy as np


def majority(fn):
    extractedstring = ""
    f_hi = open(fn)
    for cnt, line in enumerate(f_hi):
        if cnt == 0:
            continue
        else:
            elems = line.split(',')
            if elems[6][0] == '<':
                continue
            if np.log2(float(elems[6]) / 10) % 1 == 0:
                extractedstring = extractedstring + line
    f_hi.close()
    outputfn = fn[0:-4] + "_extracted.csv"
    open(outputfn, 'w').write(extractedstring)


def minority(fn):
    extractedstring = ""
    f_hi = open(fn)
    for cnt, line in enumerate(f_hi):
        if cnt == 0:
            continue
        else:
            elems = line.split(',')
            if elems[6][0] == '<':
                continue
            if not np.log2(float(elems[6]) / 10) % 1 == 0:
                extractedstring = extractedstring + line
    f_hi.close()
    outputfn = fn[0:-4] + "_minority.csv"
    open(outputfn, 'w').write(extractedstring)
