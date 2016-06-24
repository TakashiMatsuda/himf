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


def randomizedata():
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv'
    ratings = readdata.readHIdata(fn_hi)

    # make sure that the ratings a properly shuffled
    np.random.shuffle(ratings)
    np.save('ratings.npy', ratings)


def _himf_rt(LATENTDIM, REG, EXPERIMENTNUM):
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
    model = RSVD.train(LATENTDIM, train, dims, probeArray=val,
                       learnRate=0.0005, regularization=REG, nmfflag=True)

    sqerr = 0.0

    reslist = []
    for strainID, serumID, rating in test:
        err = rating - model(strainID, serumID)
        reslist.append([rating, model(strainID, serumID)])
        sqerr += err * err
    sqerr /= test.shape[0]
    return reslist
#    print np.array(reslist)
#    np.save('bestparam-res.npy', np.array(reslist))


def _himf(LATENTDIM, REG, EXPERIMENTNUM):
    """
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

    """
        get the average score
        NMF
    """
    model = RSVD.train(LATENTDIM, train, dims, probeArray=val,
                       learnRate=0.0005, regularization=REG, nmfflag=False)

    sqerr = 0.0

#    reslist = []
    for strainID, serumID, rating in test:
        err = rating - model(strainID, serumID)
#        reslist.append([rating, model(strainID, serumID)])
        sqerr += err * err
    sqerr /= test.shape[0]
#    print np.array(reslist)
#    np.save('bestparam-res.npy', np.array(reslist))

    f = open('./experiment{0}/rmse-ldim-{1}-reg-{2}'.format(EXPERIMENTNUM, LATENTDIM, REG), 'a')
    f.write("Test RMSE: {0}\n".format(np.sqrt(sqerr)))
    f.close()


if __name__ == '__main__':
#    print 'sys.argv[1]: {0}'.format(sys.argv[1])
    _himf(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
