#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

import readdata
from rsvd import RSVD
import numpy as np
import sys

exp_num = 29
klist = [1, 10, 20, 30, 40, 50]
reglist = [0., 0.01, 0.1, 0.5, 1]
nmflist = [False, True]
gammalist = [0., 0.01, 0.1, 0.5, 1]


if __name__ == "__main__":
    k = klist[int(sys.argv[1])]
    reg = reglist[int(sys.argv[3])]
    nmf = nmflist[int(sys.argv[2])]
    gamma = float(sys.argv[4])
    print exp_num, k, reg, nmf, gamma
    modelpath = "./experiment{0}/model-ldim-{1}-reg-{2}".format(
        exp_num, k, reg)
    if nmf:
        modelpath = modelpath + "-nmf"
    modelpath = modelpath + "-gamma-{0}/".format(gamma)
    model = RSVD.load(modelpath)
    fn_hi = '../H3N2_HIdata/H3N2_integrated_/H3N2_HI_data.csv'
    virusindex = readdata.readvirusindex(fn_hi)
    serumindex = readdata.readserumindex(fn_hi)
    ratings = np.load('ratings.npy')
    reslist = []
    for strainID, serumID, rating in ratings:
        pred = model(strainID, serumID)
        print (rating, pred)
        reslist.append((rating, pred))
    np.save("reslist29", np.array(reslist))
