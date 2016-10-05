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
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv'
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

    """
        get the average score
        NMF
    """
    """
    fsim = open("../cleanedseq.fa")
    simtx = simseq.simseq(virusindex, fsim)
    """
    """
    Cache date check and get simtx from cache
    """
    seq_date = os.stat("./realdata.fa").st_mtime
    simtx_date = os.stat("./simtx.npy").st_mtime
    if simtx_date <= seq_date:
        fsim = open("../realdata.fa")
        print("realdata.fa is renewed. updating simtx.npy..")
        simtx = simseq.simseq(virusindex, fsim)
        np.save("simtx.npy", simtx)
    else:
        simtx = np.load("simtx.npy")

    print "simtx"
    print(simtx)

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

    np.save(modelpath+'true_vs_prediction.npy',
            np.array(reslist))

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

    return reslist


if __name__ == '__main__':
    _himf(int(sys.argv[1]), float(sys.argv[2]),
          int(sys.argv[3]), nmfflag=int(sys.argv[4],
          gamma=int(sys.argv[5])))
