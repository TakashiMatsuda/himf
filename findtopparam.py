#!/Users/takashi/.pyenv/shims/python

import numpy as np

rmselist = [[0 for x in xrange(12)] for y in xrange(100)]
mn = 100.
mnparam = [0 for x in xrange(2)]
avgarray = np.zeros((12, 100))
lat_cnt = 0
for latentdim in xrange(1, 12, 3):
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

np.save('avgary-3.npy', avgarray)

print mnparam
