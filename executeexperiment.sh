#!/bin/sh

# 予測プログラムを走らせて、結果を収集して、
# その結果をプロットして、
# 結果を得る。

# ここで全てのパラメータを操作し、
# 他では操作しない。

# パラメータ：
# 結果の出力先

# MFの内部での
# 正則化係数
# 階数
# NMFを用いるかどうか
# 正則化の方式
# 解の探索ステップ

EXPERIMENTNUM=7
Kstart=1
Kfin=31
Kstep=5
LMstart=1
LMfin=251
LMstep=50

python run.py ${EXPERIMENTNUM} ${Kstart} ${Kfin} ${Kstep} ${LMstart} ${LMfin} ${LMstep}
# average the result by terms
python findtopparam.py ${EXPERIMENTNUM} ${Kstart} ${Kfin} ${Kstep} ${LMstart} ${LMfin} ${LMstep}
#heatmap by each parameter
python plotting.py ${EXPERIMENTNUM} ${Kstart} ${Kfin} ${Kstep} ${LMstart} ${LMfin} ${LMstep}
#predition-answer plot on the parameter that makes the best score.
python regression.py ${EXPERIMENTNUM}

