PROMPT:

ta 지표리스트 \['aberration', 'above', 'above\_value', 'accbands', 'ad', 'adosc', 'adx', 'alma', 'amat', 'ao', 'aobv', 'apo', 'aroon', 'atr', 'bbands', 'below', 'below\_value', 'bias', 'bop', 'brar', 'cci', 'cdl\_pattern', 'cdl\_z', 'cfo', 'cg', 'chop', 'cksp', 'cmf', 'cmo', 'coppock', 'cross', 'cross\_value', 'cti', 'decay', 'decreasing', 'dema', 'dm', 'donchian', 'dpo', 'ebsw', 'efi', 'ema', 'entropy', 'eom', 'er', 'eri', 'fisher', 'fwma', 'ha', 'hilo', 'hl2', 'hlc3', 'hma', 'hwc', 'hwma', 'ichimoku', 'increasing', 'inertia', 'jma', 'kama', 'kc', 'kdj', 'kst', 'kurtosis', 'kvo', 'linreg', 'log\_return', 'long\_run', 'macd', 'mad', 'massi', 'mcgd', 'median', 'mfi', 'midpoint', 'midprice', 'mom', 'natr', 'nvi', 'obv', 'ohlc4', 'pdist', 'percent\_return', 'pgo', 'ppo', 'psar', 'psl', 'pvi', 'pvo', 'pvol', 'pvr', 'pvt', 'pwma', 'qqe', 'qstick', 'quantile', 'rma', 'roc', 'rsi', 'rsx', 'rvgi', 'rvi', 'short\_run', 'sinwma', 'skew', 'slope', 'sma', 'smi', 'squeeze', 'squeeze\_pro', 'ssf', 'stc', 'stdev', 'stoch', 'stochrsi', 'supertrend', 'swma', 't3', 'td\_seq', 'tema', 'thermo', 'tos\_stdevall', 'trima', 'trix', 'true\_range', 'tsi', 'tsignals', 'ttm\_trend', 'ui', 'uo', 'variance', 'vhf', 'vidya', 'vortex', 'vp', 'vwap', 'vwma', 'wcp', 'willr', 'wma', 'xsignals', 'zlma', 'zscore'\] CustomStrategy = ta.Strategy( name="Momo and Volatility", description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20", ta=\[ {"kind": "sma", "length": 50}, {"kind": "sma", "length": 200}, {"kind": "bbands", "length": 20}, {"kind": "rsi"}, {"kind": "macd", "fast": 8, "slow": 21}, {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"}, {"kind": "ema", "length": 20}, # Exponential Moving Average {"kind": "adx"}, # Average Directional Index {"kind": "obv"}, # On-Balance Volume {"kind": "roc", "length": 14}, # Rate of Change {"kind": "atr", "length": 14}, # Average True Range {"kind": "cci"}, # Commodity Channel Index {"kind": "willr"}, # Williams %R {"kind": "stoch"}, # Stochastic Oscillator {"kind": "aroon"}, # Aroon Indicator \] ) import pandas\_ta as ta 전략에 세부지표 포함해서 모두 넣어줘

RESPONSE:

전략에 포함될 수 있는 세부 지표를 포함하여 모든 지표를 넣어드리겠습니다. 아래는 세부 지표를 포함한 전략입니다.

```python
CustomStrategy = ta.Strategy(
    name="Momo and Volatility",
    description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
    ta=[
        {"kind": "sma", "length": 50},
        {"kind": "sma", "length": 200},
        {"kind": "bbands", "length": 20},
        {"kind": "rsi"},
        {"kind": "macd", "fast": 8, "slow": 21},
        {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
        {"kind": "ema", "length": 20},  # Exponential Moving Average
        {"kind": "adx"},  # Average Directional Index
        {"kind": "obv"},  # On-Balance Volume
        {"kind": "roc", "length": 14},  # Rate of Change
        {"kind": "atr", "length": 14},  # Average True Range
        {"kind": "cci"},  # Commodity Channel Index
        {"kind": "willr"},  # Williams %R
        {"kind": "stoch"},  # Stochastic Oscillator
        {"kind": "aroon"},  # Aroon Indicator
        {"kind": "aberration"},  # Aberration
        {"kind": "above", "value": 0},  # Above
        {"kind": "above_value", "value": 0},  # Above Value
        {"kind": "accbands"},  # Acceleration Bands
        {"kind": "ad"},  # Accumulation/Distribution Line
        {"kind": "adosc"},  # Accumulation/Distribution Oscillator
        {"kind": "alma"},  # Arnaud Legoux Moving Average
        {"kind": "amat"},  # Adaptive Moving Average (TradingView)
        {"kind": "ao"},  # Awesome Oscillator
        {"kind": "aobv"},  # Adjusted On Balance Volume
        {"kind": "apo"},  # Absolute Price Oscillator
        {"kind": "atr"},  # Average True Range
        {"kind": "bbands"},  # Bollinger Bands
        {"kind": "below", "value": 0},  # Below
        {"kind": "below_value", "value": 0},  # Below Value
        {"kind": "bias"},  # Bias
        {"kind": "bop"},  # Balance of Power
        {"kind": "brar"},  # Bias Range Adjusted (Range Projection)
        {"kind": "cci"},  # Commodity Channel Index
        {"kind": "cdl_pattern"},  # Candlestick Patterns
        {"kind": "cdl_z"},  # ZigZag Candlestick Patterns
        {"kind": "cfo"},  # Chaikin Force Oscillator
        {"kind": "cg"},  # Center Of Gravity
        {"kind": "chop"},  # Choppiness Index
        {"kind": "cksp"},  # Chande Kroll Stop
        {"kind": "cmf"},  # Chaikin Money Flow
        {"kind": "cmo"},  # Chande Momentum Oscillator
        {"kind": "coppock"},  # Coppock Curve
        {"kind": "cross"},  # Cross
        {"kind": "cross_value"},  # Cross Value
        {"kind": "cti"},  # Cycle Trend Index
        {"kind": "decay"},  # Linear Decay
        {"kind": "decreasing"},  # Decreasing
        {"kind": "dema"},  # Double Exponential Moving Average
        {"kind": "dm"},  # Directional Movement
        {"kind": "donchian"},  # Donchian Channel
        {"kind": "dpo"},  # Detrended Price Oscillator
        {"kind": "ebsw"},  # Elliott Wave Breadth Spread
        {"kind": "efi"},  # Elder's Force Index
        {"kind": "ema"},  # Exponential Moving Average
        {"kind": "entropy"},  # Entropy
        {"kind": "eom"},  # Ease of Movement
        {"kind": "er"},  # Efficiency Ratio
        {"kind": "eri"},  # Elder's Elder Ray Index
        {"kind": "fisher"},  # Fisher Transform
        {"kind": "fwma"},  # Fractal Weighted Moving Average
        {"kind": "ha"},  # Heikin Ashi
        {"kind": "hilo"},  # Highest High, Lowest Low
        {"kind": "hl2"},  # HL2 (Typical Price)
        {"kind": "hlc3"},  # HLC3 (Typical Price)
        {"kind": "hma"},  # Hull Moving Average
        {"kind": "hwc"},  # Highest With Close
        {"kind": "hwma"},  # Hull Moving Average
        {"kind": "ichimoku"},  # Ichimoku Clouds
        {"kind": "increasing"},  # Increasing
        {"kind": "inertia"},  # Inertia
        {"kind": "jma"},  # Jurik Moving Average
        {"kind": "kama"},  # Kaufman Adaptive Moving Average
        {"kind": "kc"},  # Keltner Channels
        {"kind": "kdj"},  # Stochastic Oscillator (KDJ Version)
        {"kind": "kst"},  # Know Sure Thing
        {"kind": "kurtosis"},  # Kurtosis
        {"kind": "kvo"},  # Klinger Volume Oscillator
        {"kind": "linreg"},  # Linear Regression
        {"kind": "log_return"},  # Log Return
        {"kind": "long_run"},  # Long Run
        {"kind": "macd"},  # Moving Average Convergence Divergence
        {"kind": "mad"},  # Mean Absolute Deviation
        {"kind": "massi"},  # Mass Index
        {"kind": "mcgd"},  # McGinley Dynamic
        {"kind": "median"},  # Median
        {"kind": "mfi"},  # Money Flow Index
        {"kind": "midpoint"},  # Midpoint
        {"kind": "midprice"},  # Midprice
        {"kind": "mom"},  # Momentum
        {"kind": "natr"},  # Normalized Average True Range
        {"kind": "nvi"},  # Negative Volume Index
        {"kind": "obv"},  # On-Balance Volume
        {"kind": "ohlc4"},  # OHLC4 (Typical Price)
        {"kind": "pdist"},  # Price Distribution
        {"kind": "percent_return"},  # Percent Return
        {"kind": "pgo"},  # Price Gap Oscillator
        {"kind": "ppo"},  # Percentage Price Oscillator
        {"kind": "psar"},  # Parabolic Stop and Reverse (Parabolic SAR)
        {"kind": "psl"},  # Polarized Fractal Efficiency
        {"kind": "pvi"},  # Positive Volume Index
        {"kind": "pvo"},  # Percentage Volume Oscillator
        {"kind": "pvol"},  # Price Volume Trend
        {"kind": "pvr"},  # Price Volume Rank
        {"kind": "pvt"},  # Price Volume Trend
        {"kind": "pwma"},  # Previous Day Weighted Moving Average
        {"kind": "qqe"},  # QQE (Quantitative Qualitative Estimation)
        {"kind": "qstick"},  # QStick
        {"kind": "quantile"},  # Quantile
        {"kind": "rma"},  # Rau's Adaptive Moving Average
        {"kind": "roc"},  # Rate of Change
        {"kind": "rsi"},  # Relative Strength Index
        {"kind": "rsx"},  # Relative Strength Index
        {"kind": "rvgi"},  # Relative Vigor Index
        {"kind": "rvi"},  # Relative Volatility Index
        {"kind": "short_run"},  # Short Run
        {"kind": "sinwma"},  # Sine Weighted Moving Average
        {"kind": "skew"},  # Skew
        {"kind": "slope"},  # Slope
        {"kind": "sma"},  # Simple Moving Average
        {"kind": "smi"},  # Stochastic Momentum Index
        {"kind": "squeeze"},  # Squeeze Momentum Indicator
        {"kind": "squeeze_pro"},  # Squeeze Pro
        {"kind": "ssf"},  # Summed Square Filter
        {"kind": "stc"},  # Schaff Trend Cycle
        {"kind": "stdev"},  # Standard Deviation
        {"kind": "stoch"},  # Stochastic Oscillator
        {"kind": "stochrsi"},  # Stochastic RSI
        {"kind": "supertrend"},  # Supertrend
        {"kind": "swma"},  # Symmetric Weighted Moving Average
        {"kind": "t3"},  # Triple Exponential Moving Average (T3)
        {"kind": "td_seq"},  # TD Sequential
        {"kind": "tema"},  # Triple Exponential Moving Average
        {"kind": "thermo"},  # Thermometer
        {"kind": "tos_stdevall"},  # ThinkOrSwim StDevAll
        {"kind": "trima"},  # Triangular Moving Average
        {"kind": "trix"},  # Trix
        {"kind": "true_range"},  # True Range
        {"kind": "tsi"},  # True Strength Index
        {"kind": "tsignals"},  # Trend Signals
        {"kind": "ttm_trend"},  # TTM Trend
        {"kind": "ui"},  # Ulcer Index
        {"kind": "uo"},  # Ultimate Oscillator
        {"kind": "variance"},  # Variance
        {"kind": "vhf"},  # Vertical Horizontal Filter
        {"kind": "vidya"},  # Variable Index Dynamic Average
        {"kind": "vortex"},  # Vortex Indicator
        {"kind": "
```