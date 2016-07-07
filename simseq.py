#!/Users/takashi/.pyenv/shims/python

import re
import readdata
import numpy as np
from Bio.Emboss.Applications import NeedleCommandline
from Bio import AlignIO



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


def parse_getscore(fn):
    """
    not yet implemented
    """
    return 0


def similarity(x, y):
    """
    Not yet implemented
    Return: The Alignment score between x and y, those are amino acid sequences
    """
    """
    NeedleCommandline (due to the design of 'needle') needs
    the fasta sequence file.
    It doesn't accept the string.
    I create new files for each x and y sequence that are in the file.
    """
    f_x = open(".simseq_x.fa", 'w')
    f_x.write(">x\n{}".format(x))
    f_x.close()
    f_y = open(".simseq_y.fa", 'w')
    f_y.write(">y\n{}".format(y))
    f_y.close()

    needle_cline = NeedleCommandline(asequence=".simseq_x.fa",
                                     bsequence=".simseq_y.fa",
                                     gapopen=10,
                                     gapextend=0.5,
                                     outfile=".simseq_needle.txt",
                                     auto=True)
    needle_cline()
    return parse_getscore(".simseq_needle.txt")


def simseq(idx, fn):
    """
    Return : Numpy.ndarray(2d)
    File x Index -> Alignment Score Matrix
    idx : dict, (NCBI strain name : ID)
    fn : File Object pointing the fasta file
    """
    dicseq = _dicseq(fn, idx)
    m = len(dicseq)
    # TODO: Check the grammar below
    alnmtx = np.array((m, m))
    for i in xrange(m):
        for j in xrange(m):
            alnmtx[i][j] = similarity(dicseq[i], dicseq[j])
    # END*TODO
    return alnmtx


def test_simseq():
    """
    not yet implemented
    """
    fn = open("./test.fa")
    idx = readdata.readvirusindex('../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv')
    res = simseq(fn, idx)
