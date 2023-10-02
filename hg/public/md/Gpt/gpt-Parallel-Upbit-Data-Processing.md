PROMPT:

import os, pyupbit rootpath = os.path.dirname(os.path.abspath(\_\_file\_\_)) with open(f'{rootpath}/datasets/tickers.csv') as f: companies = f.read().splitlines() for company in companies: symbol = company.split(',')\[0\] df = pyupbit.get\_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1) if df is not None: print(df) df.to\_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv') else: print(f"No data available for {symbol}") 병렬처리로 수정

RESPONSE:

To modify the code for parallel processing, you can use the `multiprocessing` module in Python. Here's an updated version of your code that utilizes parallel processing using the `Pool` class from `multiprocessing`:

```python
import os
import pyupbit
import multiprocessing

def process_company(company):
    symbol = company.split(',')[0]
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)

    if df is not None:
        rootpath = os.path.dirname(os.path.abspath(__file__))
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
        return df
    else:
        print(f"No data available for {symbol}")
        return None

if __name__ == '__main__':
    rootpath = os.path.dirname(os.path.abspath(__file__))

    with open(f'{rootpath}/datasets/tickers.csv') as f:
        companies = f.read().splitlines()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    results = pool.map(process_company, companies)
    pool.close()
    pool.join()

    for result in results:
        if result is not None:
            print(result)
```

In this updated code:

1. The `process_company` function is defined, which takes a company symbol and processes it, retrieving the data and saving it to a CSV file.

2. The `multiprocessing.Pool` is created with the number of processes equal to the number of available CPU cores (`multiprocessing.cpu_count()`).

3. The `process_company` function is mapped to the list of companies using `pool.map()`, which distributes the work across multiple processes and returns the results.

4. The `pool.close()` and `pool.join()` functions are called to properly close the pool of processes and wait for all of them to finish.

5. Finally, the results are printed (if not None).

By using parallel processing, the code can process multiple companies concurrently, potentially reducing the overall execution time.

PROMPT:

동기식으로 해줘

RESPONSE:

If you prefer a synchronous (sequential) execution instead of parallel processing, you can modify the code as follows:

```python
import os
import pyupbit

rootpath = os.path.dirname(os.path.abspath(__file__))

with open(f'{rootpath}/datasets/tickers.csv') as f:
    companies = f.read().splitlines()

for company in companies:
    symbol = company.split(',')[0]
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)

    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")
```

In this modified code, the for loop iterates over the companies sequentially. It retrieves the data for each company, processes it, and saves it to a CSV file. The code waits for each iteration to complete before moving on to the next one, ensuring a synchronous execution flow.