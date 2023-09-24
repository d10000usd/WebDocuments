PROMPT:

import os import pyupbit import concurrent.futures rootpath = os.path.dirname(os.path.abspath(\_\_file\_\_)) def process\_company(company): symbol = company.split(',')\[0\] df = pyupbit.get\_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1) if df is not None: print(df) df.to\_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv') else: print(f"No data available for {symbol}") with open(f'{rootpath}/datasets/tickers.csv') as f: companies = f.read().splitlines() with concurrent.futures.ThreadPoolExecutor() as executor: executor.map(process\_company, companies) df = pyupbit.get\_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)실행할때 0.2초식 딜레이를 주고 수정

RESPONSE:

To introduce a delay of 0.2 seconds before executing the `process_company` function in the `executor.map` line, you can modify the code as follows:

```python
import os
import pyupbit
import concurrent.futures
import time

rootpath = os.path.dirname(os.path.abspath(__file__))


def process_company(company):
    symbol = company.split(',')[0]
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)

    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")


with open(f'{rootpath}/datasets/tickers.csv') as f:
    companies = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for company in companies:
            time.sleep(0.2)  # Add a delay of 0.2 seconds
            executor.submit(process_company, company)
```

In this modified code, the `time.sleep(0.2)` line is added before submitting each task to the thread pool executor. This ensures a delay of 0.2 seconds before each task is executed.