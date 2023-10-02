PROMPT:

with open(f'{rootpath}/datasets/tickers.csv') as f: companies = f.read().splitlines() for company in companies: symbol = company.split(',')\[0\] df = pyupbit.get\_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1) print(df) # df = pyupbit.get\_ohlcv(ticker=company, interval="day", count=300, to=None, period=0.1) # df = yf.download(symbol, start=first\_day\_yr\_three\_yrs\_ago, end=today) df.to\_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv') AttributeError: 'NoneType' object has no attribute 'to\_csv'

RESPONSE:

The error message you encountered suggests that the variable `df` is assigned a value of `None` in the line `df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)`. This means that the `pyupbit.get_ohlcv()` function is not returning a valid DataFrame object.

To fix this issue, you can add a check to ensure that `df` is not `None` before attempting to call the `to_csv()` method. Here's an updated version of your code that includes the necessary check:

```python
import pyupbit

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

In the updated code, we check if `df` is not `None` before proceeding with the `to_csv()` method. If `df` is `None`, it means that there is no data available for the specified symbol, and an appropriate message is printed.

PROMPT:

위에걸 가장 빠르게 pool 을 써서 수정

RESPONSE:

To modify your code using multiprocessing for faster execution, you can utilize the `multiprocessing.Pool` class to parallelize the retrieval of OHLCV data for different symbols. Here's an example of how you can implement it:

```python
import pyupbit
import multiprocessing

def process_symbol(symbol):
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)
    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")

if __name__ == '__main__':
    with open(f'{rootpath}/datasets/tickers.csv') as f:
        companies = f.read().splitlines()

    with multiprocessing.Pool() as pool:
        pool.map(process_symbol, companies)
```

In this updated code, the `process_symbol` function is defined to handle the retrieval and processing of OHLCV data for a single symbol. The `multiprocessing.Pool` class is used to create a pool of worker processes. The `pool.map()` method is then used to distribute the symbols across the worker processes, allowing for parallel execution of the `process_symbol` function.

Note that `if __name__ == '__main__':` is used to ensure that the code is only executed when running the script directly, not when it is imported as a module.

By leveraging multiprocessing, the code can concurrently process multiple symbols, potentially reducing the overall execution time.

PROMPT:

안되는데 수정

RESPONSE:

Apologies for the confusion. It seems that the `pyupbit` library is not compatible with multiprocessing due to its internal design. In this case, we can try using the `concurrent.futures` module to achieve a similar effect of parallel execution. Here's an updated version of your code using `concurrent.futures`:

```python
import pyupbit
import concurrent.futures

def process_symbol(symbol):
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)
    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")

if __name__ == '__main__':
    with open(f'{rootpath}/datasets/tickers.csv') as f:
        companies = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_symbol, companies)
```

In this updated code, we replace `multiprocessing.Pool` with `concurrent.futures.ThreadPoolExecutor`. The `executor.map()` method is used to schedule the `process_symbol` function for each symbol in the `companies` list. The `ThreadPoolExecutor` creates a pool of worker threads that can handle the processing tasks in parallel.

Please note that this uses threading instead of multiprocessing, which can still provide concurrency but may not achieve the same level of performance improvement as true parallelism.

PROMPT:

KRW-IOST,KRW-IOST KRW-RFR,KRW-RFR KRW-CVC,KRW-CVC tickers.csv 에 이렇게 들어 있어 수정해줘

RESPONSE:

Sure, I apologize for the confusion earlier. If your `tickers.csv` file contains ticker symbols in the format `KRW-XXX`, separated by commas, you can modify the code as follows to process each symbol correctly:

```python
import pyupbit
import concurrent.futures

def process_symbol(symbol):
    symbol = symbol.strip()  # Remove leading/trailing whitespaces if any
    df = pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1)
    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")

if __name__ == '__main__':
    with open(f'{rootpath}/datasets/tickers.csv') as f:
        companies = f.read().splitlines()

    symbols = [symbol.strip() for line in companies for symbol in line.split(",")]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_symbol, symbols)
```

This updated code reads the `tickers.csv` file and splits each line by commas to extract individual ticker symbols. The `strip()` method is used to remove any leading/trailing whitespaces from each symbol. The modified `symbols` list is then passed to the `executor.map()` method to process each symbol using the `process_symbol` function.

Now the code should be able to handle ticker symbols like `KRW-IOST`, `KRW-RFR`, and `KRW-CVC` correctly.

PROMPT:

비동기식으로

RESPONSE:

To modify your code to use asynchronous processing, you can utilize the `asyncio` library along with `aiohttp` for making asynchronous HTTP requests. Here's an example of how you can implement it:

```python
import asyncio
import aiohttp
import pyupbit

async def process_symbol(session, symbol):
    symbol = symbol.strip()
    df = await pyupbit.get_ohlcv(ticker=symbol, interval="day", count=300, to=None, period=0.1, session=session)
    if df is not None:
        print(df)
        df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
    else:
        print(f"No data available for {symbol}")

async def main():
    async with aiohttp.ClientSession() as session:
        with open(f'{rootpath}/datasets/tickers.csv') as f:
            companies = f.read().splitlines()
        tasks = []
        for line in companies:
            symbols = [symbol.strip() for symbol in line.split(",")]
            tasks += [process_symbol(session, symbol) for symbol in symbols]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

In this updated code, we define the `process_symbol` function as an asynchronous function. It uses `aiohttp` to make asynchronous HTTP requests to retrieve the OHLCV data for each symbol.

The `main` function is also defined as an asynchronous function. It creates an `aiohttp.ClientSession` and iterates over the lines in the `tickers.csv` file. For each line, it splits the symbols by commas, creates tasks for each symbol using the `process_symbol` function, and adds them to the `tasks` list. Finally, it uses `asyncio.gather` to run all the tasks concurrently.

The event loop is retrieved using `asyncio.get_event_loop()`, and the `main` function is run until completion using `loop.run_until_complete(main())`.

Please note that the `pyupbit` library may or may not fully support asynchronous operations. Check the documentation of `pyupbit` for more details on its async capabilities.

PROMPT:

TypeError: get\_ohlcv() got an unexpected keyword argument 'session'

RESPONSE:

I apologize for the confusion. It appears that the `pyupbit` library does not support passing a custom session object for asynchronous requests. In that case, we can use the `aiohttp` library directly to make asynchronous HTTP requests. Here's an updated version of the code that uses `aiohttp` for asynchronous processing:

```python
import asyncio
import aiohttp
import csv
import pyupbit

async def process_symbol(session, symbol):
    symbol = symbol.strip()
    url = f"https://api.upbit.com/v1/candles/days"
    params = {
        "market": symbol,
        "count": 300
    }
    async with session.get(url, params=params) as response:
        if response.status == 200:
            candles = await response.json()
            df = pyupbit.CandlestickReader(candles).df
            print(df)
            df.to_csv(f'{rootpath}/datasets/upbitdaily/{symbol}.csv')
        else:
            print(f"Failed to retrieve data for {symbol}. Status code: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        with open(f'{rootpath}/datasets/tickers.csv') as f:
            reader = csv.reader(f)
            symbols = [row[0] for row in reader]
        tasks = []
        for symbol in symbols:
            tasks.append(process_symbol(session, symbol))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

In this updated code, we use `aiohttp` to make asynchronous GET requests to the Upbit API. The `process_symbol` function takes the `session` object and the symbol as parameters. It constructs the URL and parameters for the API request, then uses `session.get` to send the request. The response is checked for a 200 status code, and if successful, the response data is converted to a DataFrame using `pyupbit.CandlestickReader`. The DataFrame is then printed and saved to a CSV file.

The `main` function is defined as an asynchronous function. It creates an `aiohttp.ClientSession` and reads the symbols from the `tickers.csv` file. It creates tasks for each symbol using the `process_symbol` function and awaits their completion using `asyncio.gather`.

Please note that this code assumes that you have the necessary dependencies (`aiohttp`, `csv`, and `pyupbit`) installed.