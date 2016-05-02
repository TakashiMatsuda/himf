#!/Users/takashi/.pyenv/shims/python

import numpy as np

rmselist = [[0 for x in xrange(40)] for y in xrange(40)]
mn = 100.
mnparam = [0 for x in xrange(2)]
avgarray = np.zeros((40, 40))
for latentdim in xrange(1, 40, 1):
    for reg in xrange(1, 40, 1):
        s = 0.
        cnt = 0
        try:
            f = open('./experiment/rmse-ldim-{0}-reg-{1}'.format(latentdim, reg/1000.0), 'r')
        except IOError:
            pass
        else:
            for line in f:
                cnt = cnt + 1
                if line.split()[2] != 'nan':
                    s = s + float(line.split()[2])

            avg = s / cnt
            if avg < mn and avg != 0.:
                mn = avg
                mnparam[0] = latentdim
                mnparam[1] = reg/1000.

            if avg == 0.:
                avg = float('nan')
                print 'allnan'
            avgarray[latentdim-1][reg-1] = avg
            print avg
            f.close()
np.save('avgary.npy', avgarray)

print mnparam
