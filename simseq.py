#!/Users/takashi/.pyenv/shims/python

import re
import readdata
import numpy as np
from Bio.Emboss.Applications import NeedleCommandline
import scipy as sp
from multiprocessing import Pool
from scipy import stats


def _dicseq(f, idx):
    """
    Return : dictionary[ordinalnumber : sequence]
    File x (Index -> strainname) -> (Index -> Sequence)
    idx : dict, (NCBI strain name : ID)
    f : File Object pointing the fasta file
    """
#    rvslist = [[x[1], x[0]] for x in idx.items()]
#    rvsdict = dict(rvslist)
    nameline = re.compile('^>')
    seqname = ""
    seq = ""
    tmp = ""
    seqdict = dict()
    seqflag = False
    for line in f:
        if nameline.match(line):
            if seqflag:
                """
                seqname : NCBI strain name
                idx : (ordinalnumber : NCBI strain name)
                rvsdict : (NCBI strain name : ordinalnumber)
                 seqdict : (ordinalnumber : Sequence)
                """
                seqdict.update({idx[tmp]: seq})
                seq = ""
            tmp = line[1:-1]
        else:
            if line[-1] == '\n':
                seq = seq + line[:-1]
            else:
                seq = seq + line[:]
            if not seqflag:
                seqflag = True
    seqdict.update({idx[tmp]: seq})
    return seqdict


def parse_getscore(fn):
    """
    Returns alignment score
    in 'fn' file.
    fn: (string) Filename of the alignment result file
    """
    f = open(fn)
    scorepattern = re.compile("Score")
    for line in f:
        if scorepattern.search(line):
            score = line.split(' ')[-1]
    f.close()
    return float(score)


def similarity(x, y, loopnum):
    """
    Return: The Alignment score between x and y, those are amino acid sequences
    """
    """
    NeedleCommandline (due to the design of 'needle') needs
    the fasta sequence file.
    It doesn't accept the string.
    I create new files for each x and y sequence that are in the file.
    """
    f_x = open(".simseq_x_{0}.fa".format(loopnum), 'w')
    f_x.write(">x\n{}".format(x))
    f_x.close()
    f_y = open(".simseq_y_{0}.fa".format(loopnum), 'w')
    f_y.write(">y\n{}".format(y))
    f_y.close()

    needle_cline = NeedleCommandline(asequence=".simseq_x_{0}.fa".format(loopnum),
                                     bsequence=".simseq_y_{0}.fa".format(loopnum),
                                     gapopen=10,
                                     gapextend=0.5,
                                     outfile=".simseq_needle_{0}.txt".format(loopnum),
                                     auto=True)
    needle_cline()
    return parse_getscore(".simseq_needle_{0}.txt".format(loopnum))


def regularizesim(alnmtx, normalflag, expflag):
    """
    All regularization for alignment matrix are
    controled in this function.
    return: regularized alnmtx
    expflag: Take exponential values of elements in given matrix
    minzero: All elements are subtracted by amin(alnmtx)
    At default, the order is as shown below:
    minzero -> expflag
    """
    if normalflag:
        alnmtx = stats.zscore(alnmtx, axis=None)
    if expflag:
        alnmtx = np.exp(alnmtx)
    return alnmtx


def simseq(idx, f):
    """
    Return : Numpy.ndarray(2d)
    File x Index -> Alignment Score Matrix
    idx : dict, (NCBI strain name : ID)
    f : File Object pointing the fasta file
    """
    dicseq = _dicseq(f, idx)
    m = len(dicseq)
    alnmtx = np.zeros((m, m))
    for i in xrange(m):
        print("calculating simtx.... "+str(i)+" in "+str(m))
        for j in xrange(m):
            alnmtx[i][j] = similarity(dicseq[i], dicseq[j], i*m + j)
    alnmtx = regularizesim(alnmtx, normalflag=True, expflag=False)
    return alnmtx


def argwrapper(args):
    return args[0](*args[1:])


def simseq_parallel(idx, f):
    """
    Parallel processing for simseq
    Return : Numpy.ndarray(2d)
    File x Index -> Alignment Score Matrix
    idx : dict, (NCBI strain name : ID)
    f : File Object pointing the fasta file
    """
    dicseq = _dicseq(f, idx)
    m = len(dicseq)
    alnmtx = np.zeros((m, m))
    for i in xrange(m):
        print("calculating simtx.... "+str(i)+" in "+str(m))

        ds_first = [dicseq[i]] * m
        loopnum_list = [x + i * m for x in range(m)]

        func_args = [(similarity, dicseq[i], dicseq[j], i * m + j) for j in range(m)]
        p = Pool(4)        
        alnmtx[i] = p.map(argwrapper, func_args)

        # alnmtx[i] = p.map(similarity, ds_first, dicseq.values(), loopnum_list)
        p.close()
        p.join()

    alnmtx = regularizesim(alnmtx, normalflag=True, expflag=False)
    return alnmtx


def test_parse_getscore():
    res = parse_getscore("../needle.txt")
    assert res == 2789.0


def test_dicseq():
    idx = readdata.readvirusindex('./test_HI.csv')
    print idx
    dicseq = _dicseq(open("test3.fa"), readdata.readvirusindex('./test_HI.csv'))
    print dicseq
    print dicseq[0]
    assert dicseq[0] == "MKTIIALSYILCLVFAQKLPGNDNSTATLCLGHHAVPNGTIVKTITNDQIEVTNATELVQSSSTGEICDSPHQILDGENCTLIDALLGDPQCDGFQNKKWDLFVERSKAYSNCYPYDVPDYASLRSLVASSGTLEFNNESFNWTGVTQNGTSSACIRRSNNSFFSRLNWLTHLKFKYPALNVTMPNNEQFDKLYIWGVHHPGTDNDQIFLYAQASGRITVSTKRSQQTVIPNIGSRPRVRNIPSRISIYWTIVKPGDILLINSTGNLIAPRGYFKIRSGKSSIMRSDAPIGKCNSECITPNGSIPNDKPFQNVNRITYGACPRYVKQNTLKLATGMRNVPEKQTRGIFGAIAGFIENGWEGMVDGWYGFRHQNSEGRGQAADLKSTQAAIDQINGKLNRLIGKTNEKFHQIEKEFSEVEGRIQDLEKYVEDTKIDLWSYNAELLVALENQHTIDLTDSEMNKLFEKTKKQLRENAEDMGNGCFKIYHKCDNACIGSIRNGTYDHDVYRDEALNNRFQIKGVELKSGYKDWILWISFAISCFLLCVALLGFIMWACQKGNIRCNICI"


def test_simseq():
    """
    passed some simple tests
    """
    f = open("./test.fa")
    idx = readdata.readvirusindex('./test_HI.csv')
    res = simseq(idx, f)
    f.close()
    print(res)


def test_simseq_parallel():
    f = open("./test.fa")
    idx = readdata.readvirusindex('./test_HI.csv')
    res = simseq(idx, f)
    f.seek(0)
    res_parallel = simseq_parallel(idx, f)
    f.close()
    assert (res == res_parallel).all()
