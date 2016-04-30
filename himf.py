#!/Users/takashi/.pyenv/shims/python

"""
    Calculate the MF for HI data
    powered by tutorial.py in PyRSVD
    Author : Takashi Matsuda 2016
    These codes are under MIT License.
"""

import numpy as np
import readdata

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
dims = (len(strainindex), len(strainindex))
print dims
print train
print val
model = RSVD.train(20, train, dims, probeArray=val, learnRate=0.0005, regularization=0.005)

sqerr = 0.0
#TODO: Edit below
for strainID, serumID, rating in test:
    err = rating - model(strainID, serumID)
    sqerr += err * err
sqerr /= test.shape[0]
print "Test RMSE: ", np.sqrt(sqerr)
