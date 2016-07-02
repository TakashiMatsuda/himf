#!/Users/takashi/.pyenv/shims/python

import re
import readdata


def simseq(fn, idx):
    """
    Return : Numpy.ndarray(2d)
    File x Index -> Alignment Score Matrix
    idx : dict, (NCBI strain name : ID)
    fn : File Object pointing the fasta file
    """
#    rvslist = [[x[1], x[0]] for x in idx.items()]
#    rvsdict = dict(rvslist)

    nameline = re.compile('^>')
    seqname = ""
    seq = ""
    seqdict = dict()
    for line in fn:
        if nameline.match(line):
            if not seqname == "":
                """
                seqname : NCBI strain name
                idx : (ordinalnumber : NCBI strain name)
                rvsdict : (NCBI strain name : ordinalnumber)
                seqdict : (ordinalnumber : Sequence)
                """
                seqdict.update({idx[seqname]: seq})
                seq = ""
            seqname = line
        else:
            seq.append(line)
    return seqdict


def test_simseq():
    """
    not yet implemented
    """
    fn = open("./test.fa")
    idx = readdata.readvirusindex('../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv')
    res = simseq(fn, idx)
