#!/Users/takashi/.pyenv/shims/python

"""
    Calculate the MF for HI data
    powered by PyRSVD
    Author : Takashi Matsuda 2016
    These codes are under MIT License.
"""

import numpy as np
import readdata
import sys
import simseq
import os


def randomizedata():
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data_minority.csv'
    ratings = readdata.readHIdata(fn_hi)
    # make sure that the ratings a properly shuffled
    np.random.shuffle(ratings)
    np.save('ratings.npy', ratings)


def _himf_rt(LATENTDIM, REG, nmfflag, gamma):
    """
    deprecated function
    """
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv'
    virusindex = readdata.readvirusindex(fn_hi)
    serumindex = readdata.readserumindex(fn_hi)
    ratings = np.load('ratings.npy')

    # create train, validation and test sets.
    n = int(ratings.shape[0]*0.8)
    train = ratings[:n]
    test = ratings[n:]
    v = int(train.shape[0]*0.9)
    # split train to 1(validate) : 9(training)
    val = train[v:]
    train = train[:v]
    from rsvd import RSVD
    dims = (len(virusindex), len(serumindex))

    #  get the similarity score
    seq_date = os.stat("./realdata.fa").st_mtime
    simtx_date = os.stat("./simtx.npy").st_mtime
    if simtx_date <= seq_date:
        fsim = open("../realdata.fa")
        print("realdata.fa is renewed. updating simtx.npy..")
        simtx = simseq.simseq(virusindex, fsim)
        np.save("simtx.npy", simtx)
    else:
        simtx = np.load("simtx.npy")

    model = RSVD.train(LATENTDIM, train, dims, simtx,
                       probeArray=None, maxEpochs=500,
                       learnRate=0.001, regularization=REG, nmfflag=nmfflag,
                       randomNoise=5.,
                       gamma=gamma)

    reslist = []
    for strainID, serumID, rating in test:
        reslist.append([rating, model(strainID, serumID)])
    return reslist


def _himf(LATENTDIM, REG, EXPERIMENTNUM, gamma,
          nmfflag=None, lr=0.001, esflag=True):
    """
    Main part of himf
    She prepares the dataset from H3N2_HI_data.csv.
    She needs ratings.npy got ready.
    LATENTDIM: the number of the rank of the matrix calculated
    REG: alpha variable
    EXPERIMENTNUM: the number of the experiment for keep it in order
    gamma: the parametric variable
    that control the strength of the normalization by sequences
    nmfflag: search only Non-negative Matrix if it is True
    lr: learning step size of SGD
    esflag : Early stopping applied if it is True
    """
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data_minority.csv'
    virusindex = readdata.readvirusindex(fn_hi)
    serumindex = readdata.readserumindex(fn_hi)
    ratings = np.load('ratings.npy')

    # create train, validation and test sets.
    n = int(ratings.shape[0] * 0.8)
    train = ratings[:n]
    test = ratings[n:]
    v = int(train.shape[0] * 0.9)
    # split train to 1(validate) : 9(training)
    val = train[v:]
    train = train[:v]
    from rsvd import RSVD
    dims = (len(virusindex), len(serumindex))

    """
        get the average score
        NMF
    """

    """
    Cache date check and get simtx from cache
    -> Off for first experiment of minority
    """
#    seq_date = os.stat("./realdata_minority.fa").st_mtime
#    simtx_date = os.stat("./simtx_minority.npy").st_mtime
#    if simtx_date <= seq_date:
    fsim = open("../realdata_minority.fa")
    print("making simtx_minority.npy..")
    simtx = simseq.simseq(virusindex, fsim)
    np.save("simtx_minority.npy", simtx)
#    else:
#        simtx = np.load("simtx_minority.npy")

    model = RSVD.train(LATENTDIM, train, dims, simtx,
                       probeArray=val, esflag=esflag, maxEpochs=1000,
                       learnRate=lr,
                       regularization=REG,
                       nmfflag=nmfflag,
                       randomNoise=0.1,
                       gamma=gamma)

    sqerr = 0.0

    reslist = []
    for strainID, serumID, rating in test:
        err = rating - model(strainID, serumID)
        reslist.append([rating, model(strainID, serumID)])
        sqerr += err * err
    sqerr /= test.shape[0]

    modelpath = "./experiment{0}/model-ldim-{1}-reg-{2}".format(
                EXPERIMENTNUM, LATENTDIM, REG)
    rmsepath = "./experiment{0}/rmse-ldim-{1}-reg-{2}".format(
                EXPERIMENTNUM, LATENTDIM, REG)
    if nmfflag:
        modelpath = modelpath + "-nmf"
        rmsepath = rmsepath + "-nmf"
    modelpath = modelpath + "-gamma-{0}".format(gamma)
    rmsepath = rmsepath + "-gamma-{0}".format(gamma)
    modelpath = modelpath + "/"

    if not os.path.exists(os.path.dirname(modelpath)):
        try:
            os.makedirs(os.path.dirname(modelpath))
            model.save(modelpath)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    f = open(rmsepath, 'a+')
    print "Test RMSE: {0}\n".format(np.sqrt(sqerr))
    f.write("Test RMSE: {0}\n".format(np.sqrt(sqerr)))
    f.close()

    np.save(modelpath + 'true_vs_prediction.npy',
            np.array(reslist))

    return reslist


if __name__ == '__main__':
    _himf(int(sys.argv[1]), float(sys.argv[2]),
          int(sys.argv[3]), nmfflag=int(sys.argv[4],
          gamma=int(sys.argv[5])))
