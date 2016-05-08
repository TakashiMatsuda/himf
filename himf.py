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


def himf(LATENTDIM, REG):
    fn_index = '../H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv'
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv'
    strainindex = readdata.readindex(fn_index)
    ratings = readdata.readHIdata(fn_hi, strainindex)
    print ratings
    # make sure that the ratings a properly shuffled
    np.random.shuffle(ratings)

    # create train, validation and test sets.
    n = int(ratings.shape[0]*0.8)
    train = ratings[:n]
    test = ratings[n:]
    v = int(train.shape[0]*0.9)
    # split train to 1(validate) : 9(training)
    val = train[v:]
    train = train[:v]

    from rsvd import RSVD
#    dims = (len(strainindex), len(strainindex))
    print len(strainindex)
    dims = (402, 214)
    model = RSVD.train(LATENTDIM, train, dims, probeArray=val, learnRate=0.0005, regularization=REG)

    sqerr = 0.0

    reslist = []
    for strainID, serumID, rating in test:
        err = rating - model(strainID, serumID)
        reslist.append([rating, model(strainID, serumID)])
        sqerr += err * err
    sqerr /= test.shape[0]
#    print np.array(reslist)
#    np.save('bestparam-res.npy', np.array(reslist))

    f = open('./experiment2/rmse-ldim-{0}-reg-{1}'.format(LATENTDIM, REG), 'a')
    f.write("Test RMSE: {0}\n".format(np.sqrt(sqerr)))
    f.close()

    print "Test RMSE: ", np.sqrt(sqerr)


if __name__ == '__main__':
#    print 'sys.argv[1]: {0}'.format(sys.argv[1])
    himf(int(sys.argv[1]), float(sys.argv[2]))
