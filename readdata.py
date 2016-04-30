#!/Users/takashi/.pyenv/shims/python


def readindex(filename):
    """
    return the dictionary
    """
    f_dic = open(filename)
    strain_index = dict()
    for cnt, line in enumerate(f_dic):
        if cnt == 0:
            continue
        line.split(',')[0]
        strain_index.update({line.split(',')[0]: cnt-1})

    return strain_index


def readHIdata(filename):
    """
    not yet implemented
    """
    return 0


def test_readindex():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv"
    res = readindex(filename)
    assert res['A/Akita/4/1993'] == 0


def test_readHIdata():
    filename = "../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.tsv"
    res = readHIdata(filename)
    assert res[0][0] == 5120
