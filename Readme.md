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
