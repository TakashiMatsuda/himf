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


def readserumindex(filename):
    """
    return the dictionary such as
    {serumstrain:index}
    filename: the name of the strain list file
    """
    f_dic = open(filename)
    strain_index = dict()
    idcnt = 0
    for cnt, line in enumerate(f_dic):
        if cnt == 0:
            continue
        elif line.split(',')[4] not in strain_index:
            strain_index.update({line.split(',')[4]: idcnt})
            idcnt += 1

    f_dic.close()
    return strain_index


def readvirusindex(filename):
    """
    return the dictionary such as
    {serumstrain:index}
    filename: the name of the strain list file
    """
    f_dic = open(filename)
    strain_index = dict()
    idcnt = 0
    for cnt, line in enumerate(f_dic):
        if cnt == 0:
            continue
        elif line.split(',')[1] not in strain_index:
            strain_index.update({line.split(',')[1]: idcnt})
            idcnt += 1

    f_dic.close()
    return strain_index


def readHIdata(filename):
    """
    return ndarray whose elements are tuples as follows
    (StrainID, SerumID, HIvalue)
    the type is
    (uint4, uint4, f4)
    """
    # f_hi: datafile
    serumindex = readserumindex(filename)
    virusindex = readvirusindex(filename)
    f_hi = open(filename)
    # mold_hiarray: each element is ...
    mold_hiarray = []
    for cnt, line in enumerate(f_hi):
        if cnt == 0:
            continue

        parse = line.split(',')
        # TODO: the entry that its value is out of range also should be
        # entered into calculation
        if parse[6][0] == '<':
            continue
#        elif parse[1] not in strainindex or parse[4] not in strainindex:
        else:
            # movie is 1 origin!
            mold_hiarray.append((virusindex[parse[1]]+1,
                                 serumindex[parse[4]],
                                 math.log(float(parse[6]), 2)))

    f_hi.close()
    res = np.array(mold_hiarray, dtype=np.dtype("H,I,f4"))
    print res
    return res


def test_readindex():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv"
    res = readindex(filename)
    assert res['A/Akita/4/1993'] == 0


def test_readvirusindex():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv"
    res = readvirusindex(filename)
    assert res['A/Wisconsin/67/2005'] == 0



def test_readHIdata():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv"
    strainindex = readindex("../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv")
    serumindex = readserumindex("../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv")
    virusindex = readvirusindex("../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv")
    res = readHIdata(filename)
    assert (virusindex['A/Wisconsin/67/2005'], serumindex['A/Wisconsin/67/2005'], math.log(5120.0, 2)) in res
