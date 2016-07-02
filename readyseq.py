#!/Users/takashi/.pyenv/shims/python

import re

fn = "H3N2_HIdata/H3N2_integrated_/H3N2_seq_data.csv"
fnseq = "H3N2_HIdata/H3N2_integrated_/HIsequence.fa"
f = open(fn)
fw = open("cleanedseq.fa", 'w')
cnt = 0
nacount = 0
namepattern = re.compile("^>")
seq = ""
for line in f:
    print cnt
    if cnt == 0:
        cnt = 1
        continue
    else:
        cnt += 1
    name = line.split(',')[0]
    shortname = name[:-4] + name[-2:]
    seqflag = False
    fseq = open(fnseq)
    for l2 in fseq:
        if namepattern.search(l2[:-1]):
            if seqflag:
                break
            elif name == l2[1:-1] or shortname == l2[1:-1]:
                seqflag = True
                seq = ""
            continue
        elif seqflag:
            seq = seq + l2[:-1]
            continue

    fw.write('\n'+name+'\n'+seq)
    if seq == "":
        fw.write('***')
        nacount += 1
    seq = ""
    fseq.close()

print "The rate of NA is {0} / {1}".format(nacount, cnt)
fw.close()
f.close()

