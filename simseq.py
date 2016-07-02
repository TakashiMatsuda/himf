#!/Users/takashi/.pyenv/shims/python

import re
import readdata
import numpy as np

def _dicseq(fn, idx):
    """
    Return : dictionary[ordinalnumber : sequence]
    File x (Index -> strainname) -> (Index -> Sequence)
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


def similarity(seq, seq):
    """
    Not yet implemented
    """
    return 0


def simseq(idx, fn):
    """
    Return : Numpy.ndarray(2d)
    File x Index -> Alignment Score Matrix
    idx : dict, (NCBI strain name : ID)
    fn : File Object pointing the fasta file
    """
    dicseq = _dicseq(fn, idx)
    m = len(dicseq)
    ##### TODO: Check the grammar below
    alnmtx = np.array((m, m))
    for i in xrange(m):
        for j in xrange(m):
            alnmtx[i][j] = similarity(dicseq[i], dicseq[j])
    ##### END*TODO
    return alnmtx


def test_simseq():
    """
    not yet implemented
    """
    fn = open("./test.fa")
    idx = readdata.readvirusindex('../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv')
    res = simseq(fn, idx)
