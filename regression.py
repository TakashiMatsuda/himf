#!/usr/bin/python

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import sys
import himf

mnparam = np.load('bestparam-{0}'.npy.format(sys.argv[1]))
data = []
for i in xrange(100):
    himf.randomizedata()
    data = data + himf._himf_rt(mnparam[0], mnparam[1], sys.argv[1])

xlist = []
ylist = []
for i, elem in enumerate(data):
    xlist.append(data[i][0])
    ylist.append(data[i][1])

x = np.array(xlist)
y = np.array(ylist)

nsample = x.size
X = np.column_stack((np.repeat(1, nsample), x))
model = sm.OLS(y, X)
results = model.fit()
print results.summary()

a, b = results.params

fig, ax = plt.subplots()
plt.plot(x, y, 'o')
plt.plot(x, a+b*x, label="a+b*x")
plt.legend(loc=2)
plt.title('True-Predictedvalue', fontsize=20)
plt.grid('on')
regl_str = "a={:8.3f}, b={:8.3f}".format(a, b)
plt.text(2.3, 11.5, regl_str)
plt.text(2.3, 11, "pearson r = 0.353")

#p1 = plt.Rectangle((0, 0), 1, 1, fc="green")
#plt.legend([p1], ["r = 0.353"])

plt.xlabel("True value", fontsize=24)
plt.ylabel("Predicted value", fontsize=24)

fig.savefig('bestparam-plot-{0}.pdf'.format(sys.argv[1]))
plt.show()
