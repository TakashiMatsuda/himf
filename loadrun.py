#!/Users/takashi/.pyenv/shims/python
# -*- coding:utf-8 -*-

"""
saveした、あるパラメータ設定のrsvdmodelを、
キャッシュから呼び出して使うためのスクリプト
"""


import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

exp_num = 29
if __name__ == '__main__':
    reslist = np.load("strongnmfreslist29.npy")
    ##
    # plotting procedure
    ##
    xlist = []
    ylist = []
    for i, elem in enumerate(reslist):
        xlist.append(reslist[i][0])
        ylist.append(reslist[i][1])

    x = np.array(xlist)
    y = np.array(ylist)

    nsample = x.size
    X = np.column_stack((np.repeat(1, nsample), x))
#    model = sm.OLS(y, X)
#    results = model.fit()
#    print results.summary()

#    a, b = results.params

    fig, ax = plt.subplots()
    plt.plot(x, y, 'o')
    plt.plot(x, x, label="y=x")
    plt.legend(loc=2)
    plt.title('True-Prediction plot k=10,lambda=0.01,gamma=0.0,NMF', fontsize=14)
    plt.grid('on')
#    regl_str = "a={:8.3f}, b={:8.3f}".format(a, b)
#    plt.text(2.3, 11.5, regl_str)
#    plt.text(2.3, 11, "pearson r = 0.353")

    p1 = plt.Rectangle((0, 0), 1, 1, fc="green")
#    plt.legend([p1], ["r = 0.353"])

    plt.xlabel("True value", fontsize=12)
    plt.ylabel("Predicted value", fontsize=12)

    fig.savefig('nature-of-purenmf.pdf'.format(exp_num))
    plt.show()
