PROMPT:

import os import glob,csv import pyupbit import pandas as pd import talib as tl from patterns import patterns from flask import Flask, request,render\_template,url\_for rootpath = os.path.dirname(os.path.abspath(\_\_file\_\_)) pattern = { 'CDL2CROWS':'Two Crows', 'CDL3BLACKCROWS':'Three Black Crows', 'CDL3INSIDE':'Three Inside Up/Down', 'CDL3LINESTRIKE':'Three-Line Strike', 'CDL3OUTSIDE':'Three Outside Up/Down', 'CDL3STARSINSOUTH':'Three Stars In The South', 'CDL3WHITESOLDIERS':'Three Advancing White Soldiers', 'CDLABANDONEDBABY':'Abandoned Baby', 'CDLADVANCEBLOCK':'Advance Block', 'CDLBELTHOLD':'Belt-hold', 'CDLBREAKAWAY':'Breakaway', 'CDLCLOSINGMARUBOZU':'Closing Marubozu', 'CDLCONCEALBABYSWALL':'Concealing Baby Swallow', 'CDLCOUNTERATTACK':'Counterattack', 'CDLDARKCLOUDCOVER':'Dark Cloud Cover', 'CDLDOJI':'Doji', 'CDLDOJISTAR':'Doji Star', 'CDLDRAGONFLYDOJI':'Dragonfly Doji', 'CDLENGULFING':'Engulfing Pattern', 'CDLEVENINGDOJISTAR':'Evening Doji Star', 'CDLEVENINGSTAR':'Evening Star', 'CDLGAPSIDESIDEWHITE':'Up/Down-gap side-by-side white lines', 'CDLGRAVESTONEDOJI':'Gravestone Doji', 'CDLHAMMER':'Hammer', 'CDLHANGINGMAN':'Hanging Man', 'CDLHARAMI':'Harami Pattern', 'CDLHARAMICROSS':'Harami Cross Pattern', 'CDLHIGHWAVE':'High-Wave Candle', 'CDLHIKKAKE':'Hikkake Pattern', 'CDLHIKKAKEMOD':'Modified Hikkake Pattern', 'CDLHOMINGPIGEON':'Homing Pigeon', 'CDLIDENTICAL3CROWS':'Identical Three Crows', 'CDLINNECK':'In-Neck Pattern', 'CDLINVERTEDHAMMER':'Inverted Hammer', 'CDLKICKING':'Kicking', 'CDLKICKINGBYLENGTH':'Kicking - bull/bear determined by the longer marubozu', 'CDLLADDERBOTTOM':'Ladder Bottom', 'CDLLONGLEGGEDDOJI':'Long Legged Doji', 'CDLLONGLINE':'Long Line Candle', 'CDLMARUBOZU':'Marubozu', 'CDLMATCHINGLOW':'Matching Low', 'CDLMATHOLD':'Mat Hold', 'CDLMORNINGDOJISTAR':'Morning Doji Star', 'CDLMORNINGSTAR':'Morning Star', 'CDLONNECK':'On-Neck Pattern', 'CDLPIERCING':'Piercing Pattern', 'CDLRICKSHAWMAN':'Rickshaw Man', 'CDLRISEFALL3METHODS':'Rising/Falling Three Methods', 'CDLSEPARATINGLINES':'Separating Lines', 'CDLSHOOTINGSTAR':'Shooting Star', 'CDLSHORTLINE':'Short Line Candle', 'CDLSPINNINGTOP':'Spinning Top', 'CDLSTALLEDPATTERN':'Stalled Pattern', 'CDLSTICKSANDWICH':'Stick Sandwich', 'CDLTAKURI':'Takuri (Dragonfly Doji with very long lower shadow)', 'CDLTASUKIGAP':'Tasuki Gap', 'CDLTHRUSTING':'Thrusting Pattern', 'CDLTRISTAR':'Tristar Pattern', 'CDLUNIQUE3RIVER':'Unique 3 River', 'CDLUPSIDEGAP2CROWS':'Upside Gap Two Crows', 'CDLXSIDEGAP3METHODS':'Upside/Downside Gap Three Methods' } stocks = {} with open(f'{rootpath}/datasets/tickers.csv') as f: for row in csv.reader(f): if '\\ufeff' in row\[0\] : row\[0\] = row\[0\].replace('\\ufeff', '') stocks\[row\[0\]\] = {'company': row\[1\]} print(stocks) if pattern: datafiles = os.listdir(f'{rootpath}/datasets/upbitdaily') for dataset in datafiles: df = pd.read\_csv(f'{rootpath}/datasets/upbitdaily/{dataset}') pattern\_function = getattr(tl, pattern) symbol = dataset.split('.')\[0\] try: result = pattern\_function(df\['Open'\],df\['High'\],df\['Low'\],df\['Close'\]) last = result.tail(1).values\[0\] if last > 0: stocks\[symbol\]\[pattern\] = 'bullish' elif last < 0: stocks\[symbol\]\[pattern\] = 'bearish' else: stocks\[symbol\]\[pattern\] = None except: pass 수정해줘 pattern\_function = getattr(tl, pattern) TypeError: attribute name must be string, not 'dict'

RESPONSE:

The error message indicates that the `pattern` variable is a dictionary, but the `getattr` function expects the attribute name to be a string.

To resolve this issue, you need to iterate over the keys of the `pattern` dictionary and retrieve the pattern function for each key. Here's an updated version of your code:

```python
# ...

if patterns:
    datafiles = os.listdir(f'{rootpath}/datasets/upbitdaily')
    for dataset in datafiles:
        df = pd.read_csv(f'{rootpath}/datasets/upbitdaily/{dataset}')

        symbol = dataset.split('.')[0]
        for pattern_key in patterns.keys():
            pattern_function = getattr(tl, pattern_key)
            try:
                result = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = result.tail(1).values[0]
                if last > 0:
                    stocks[symbol][patterns[pattern_key]] = 'bullish'
                elif last < 0:
                    stocks[symbol][patterns[pattern_key]] = 'bearish'
                else:
                    stocks[symbol][patterns[pattern_key]] = None
            except:
                pass
```

In this updated code, the `pattern_key` variable represents each key in the `patterns` dictionary, and `patterns[pattern_key]` retrieves the corresponding pattern name.