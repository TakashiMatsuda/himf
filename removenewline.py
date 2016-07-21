#!/Users/takashi/.pyenv/shims/python

"""
remove extra newlines in 'cleanedseq.fa'
"""
import re

headpattern = re.compile('^>')

f_old = open('./cleanedseq.fa', 'r')
resultstr = ""
for line in f_old:
    if headpattern.search(line):
        resultstr = resultstr + '\n' + line
    else:
        resultstr = resultstr + line[:-1]
f_old.close()
f_new = open('./realdata.fa', 'w')
f_new.write(resultstr)
f_new.close()
