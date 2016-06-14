#!/Users/takashi/.pyenv/shims/python

import numpy as np
import sys

params = [int(x) for x in sys.argv[1:]]
rmselist = [[0 for x in xrange(params[2] - 1)] for y in xrange(params[5] - 1)]
mn = 100.
mnparam = [0 for x in xrange(2)]
avgarray = np.zeros((21, 6))
lat_cnt = 0
for latentdim in xrange(params[1], params[2], params[3]):
    for reg in xrange(params[4], params[5], params[6]):
        s = 0.
        cnt = 0
        try:
            f = open('./experiment{0}/rmse-ldim-{1}-reg-{2}'.format(sys.argv[1], latentdim, reg/1000.0), 'r')
            print f
        except IOError:
            avg = float('inf')
        else:
            for line in f:
                if line.split()[2] != 'nan':
                    cnt = cnt + 1
                    s = s + float(line.split()[2])

            if cnt <= 50 or s == 0.:
                avg = float('inf')
            else:
                avg = s / cnt
                if avg < mn and avg != 0.:
                    mn = avg
                    mnparam[0] = latentdim
                    mnparam[1] = reg/1000.
            f.close()

        avgarray[lat_cnt][(reg/50)] = avg
        print avg

    lat_cnt += 1

"""
for latentdim in xrange(12, 24, 3):
    for reg in xrange(1, 300, 3):
        s = 0.
        cnt = 0
        try:
            f = open('./experiment3/rmse-ldim-{0}-reg-{1}'.format(latentdim, reg/1000.0), 'r')
            print f
        except IOError:
            pass
        else:
            for line in f:
                if line.split()[2] != 'nan':
                    cnt = cnt + 1
                    s = s + float(line.split()[2])

            if cnt == 0:
                avg = float('inf')
            else:
                avg = s / cnt
                if avg < mn and avg != 0.:
                    mn = avg
                    mnparam[0] = latentdim
                    mnparam[1] = reg/1000.

            print avg
            avgarray[lat_cnt][(reg/3)-1] = avg
            f.close()
    lat_cnt += 1

for latentdim in xrange(24, 36, 3):
    for reg in xrange(1, 300, 3):
        s = 0.
        cnt = 0
        try:
            f = open('./experiment3/rmse-ldim-{0}-reg-{1}'.format(latentdim, reg/1000.0), 'r')
            print f
        except IOError:
            pass
        else:
            for line in f:
                if line.split()[2] != 'nan':
                    cnt = cnt + 1
                    s = s + float(line.split()[2])

            if cnt == 0:
                avg = float('inf')
            else:
                avg = s / cnt
                if avg < mn and avg != 0.:
                    mn = avg
                    mnparam[0] = latentdim
                    mnparam[1] = reg/1000.

            print avg
            avgarray[lat_cnt][(reg/3)-1] = avg
            f.close()
    lat_cnt += 1
"""

np.save('avgary-{0}.npy'.format(sys.argv[1]), avgarray)

np.save('bestparam-{0}.npy'.format(sys.argv[1]), mnparam)
print(mnparam)
