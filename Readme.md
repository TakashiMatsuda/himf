#つかいかた
himfを実行。
himfの実行文は下の文

```
if __name__ == '__main__':
\#    print 'sys.argv[1]: {0}'.format(sys.argv[1])
    _himf(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
```

_himfは

```
def _himf(LATENTDIM, REG, EXPERIMENTNUM):
```

#実験の流れ
executeexpreiment.sh -> main.py -> himf.py
executeexperiment.sh : 網羅的な実験の為の範囲決め, 実験番号を決める。
run.py : 実際に各パラメータについてプロセスを立ててhimf.pyを実行する

##プロット
予測結果を正解値と比較する：
python show-predict-true.py $EXPERIMENTNUM

## New flow to work
一連の流れはexp_numで管理される。
main.py => himf.py
main.pyがexp_numと各パラメータの振り方を定める。
キャッシュとして保存するので
下流のスクリプトはそれを参照しなければならない。
>
getavg_score.py
各パラメータでのRMSE結果を平均する。
>
heatplot.py
各パラメータでの平均RMSE結果をheatmapに可視化する。
>
