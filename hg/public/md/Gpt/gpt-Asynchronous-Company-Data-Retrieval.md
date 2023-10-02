PROMPT:

import os, pyupbit rootpath = os.path.dirname(os.path.abspath(\_\_file\_\_)) with open(f'{rootpath}/datasets/tickers.csv') as f: companies = f.read().splitlines() for company in companies: symbol = company.split(',')\[0\] df = pyupbit.get\_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1) if df is not None: print(df) df.to\_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv') else: print(f"No data available for {symbol}") 비동기식으로 pool 써서 수정

RESPONSE:

To modify the code to use a pool for asynchronous execution, you can utilize the `concurrent.futures` module in Python. Here's an example of how you can modify your code:

```python
import os
import pyupbit
import concurrent.futures

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
        executor.map(process_company, companies)
```

In the modified code, the `process_company` function is created to process each company asynchronously. The `ThreadPoolExecutor` is used as the executor to manage the pool of threads. The `executor.map` method is used to map the `process_company` function to each company in the `companies` list, which allows for concurrent execution.

Please note that the modified code uses threads for concurrency, which is suitable for I/O-bound tasks like network requests. However, if you have CPU-bound tasks, you might consider using processes instead. The `concurrent.futures.ProcessPoolExecutor` can be used as an alternative to `ThreadPoolExecutor` for process-based concurrency.