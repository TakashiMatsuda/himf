#!/Users/takashi/.pyenv/shims/python

import numpy as np
import math


def readindex(filename):
    """
    return the dictionary such as
    {strain:index}
    filename: the name of the strain list file
    """
    f_dic = open(filename)
    strain_index = dict()
    for cnt, line in enumerate(f_dic):
        if cnt == 0:
            continue
        strain_index.update({line.split(',')[0]: cnt-1})

    f_dic.close()
    return strain_index


def readHIdata(filename, strainindex):
    """
    return ndarray whose elements are tuples as follows
    (StrainID, SerumID, HIvalue)
    the type is
    (uint4, uint4, f4)
    """

    lenfhi = sum(1 for line in open(filename))
    f_hi = open(filename)
    mold_hiarray = []
    for cnt, line in enumerate(f_hi):
        if cnt == 0:
            continue

        parse = line.split(',')
        # TODO: the entry that its value is out of range also should be
        # into calculation
        if parse[6][0] == '<':
            continue
        elif parse[1] not in strainindex or parse[4] not in strainindex:
            continue
        else:
            mold_hiarray.append((strainindex[parse[1]],
                                 strainindex[parse[4]],
                                 math.log(float(parse[6]), 2)))

    f_hi.close()
    return np.array(mold_hiarray, dtype=np.dtype("H,I,f4"))


def test_readindex():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv"
    res = readindex(filename)
    assert res['A/Akita/4/1993'] == 0


def test_readHIdata():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv"
    strainindex = readindex("../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv")
    res = readHIdata(filename, strainindex)
    assert (strainindex['A/Wisconsin/67/2005'], strainindex['A/Wisconsin/67/2005'], math.log(5120, 2)) in res
