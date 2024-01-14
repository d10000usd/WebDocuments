import yfinance as yf
import pandas as pd
import multiprocessing
from pykrx import stock
import json
import pandas_ta as ta
# 다운로드할 Ticker 리스트
from datetime import datetime
import os,re ,sys,warnings
import requests
# from tabulate import tabulate
from PIL import Image, ImageDraw, ImageFont
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import shutil
from backtesting.test import SMA
# import vectorbt as vbt
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("default", category=FutureWarning)


import plotly.graph_objects as go

# import main_sub_캔들다운_백테스트_vue3_차트 as vue3chart
# 각 Ticker를 다운로드하고 DataFrame으로 변환하는 함수
# 오류(SettingWithCopyError 발생)
# pd.set_option('mode.chained_assignment', 'raise') # SettingWithCopyError

# 경고(SettingWithCopyWarning 발생, 기본 값입니다)
# pd.set_option('mode.chained_assignment', 'warn') # SettingWithCopyWarning
pd.set_option('mode.chained_assignment',  None) # <==== 경고를 끈다

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def LOGMODULE(fname):
    ##LOGMODULE(sys._getframe().f_code.co_name) 함수내부에서 다른함수를 참조하면 사용
    ## print(LOGMODULE(sys._getframe().f_code.co_name)) 외부함수 참조가 없으면 사용
    lenth = len(fname)
    prCyan(" - ["+str(fname).ljust(lenth)+"]")
    return "-"




class GetTickerFromStock:
    def __init__(self,category,etfcode):
        # KOSPI = 'KS'
        # KOSDAQ = 'KQ'
  
        self.CATEGORY = category
        self.ETFCODE = etfcode
        self.staticpath = "/Users/hg/DEV/WebDocuments/public/DailyInfo/configdict.json"
        self.stockticker = pd.read_csv("/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/csv/stockTicker.csv")
        self.configdict = self.open_configdict("/Users/hg/DEV/WebDocuments/public/json/configdict.json")
        self.datasetspath = "/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/datasets/koreadaily"
    def open_configdict(self,config_dict_path):
        if os.path.exists(config_dict_path):
            with open(config_dict_path, 'r') as file:
                config_dict = json.load(file)    
        return config_dict
    def read_csv(self, path):
        pass
    def save_csv(self, path):
        # Implement your code to save data to a CSV file here.
        pass

    def save_json(self, path):
        # Implement your code to save data to a JSON file here.
        pass

    def get_ohlc_yahoo(self):
        pass
    

    def ohlc_analysis(self, category):
        # Implement your OHLC analysis code here based on the 'category'.
        pass

    def strategies_Adj(self):
        ta_custom_indicators = self.configdict['strategies_stock']['ta']
        ta_custom_patterns = self.configdict['strategies_pattern']['combinded']
        df = pd.read_csv("/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/datasets/koreadaily/348370KQ.csv", index_col='Date')



        # df.index = pd.to_datetime(df.index)
        # df.reset_index(inplace=True)
        # df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
        # df.loc[:, 'Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

        df.index = pd.to_datetime(df.index)
        df.reset_index(inplace=True)
        # 'Date' 열을 datetime 형식으로 변환하고, 날짜 형식을 지정하여 다시 문자열로 변환합니다.
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

        # 위와 같은 목적으로 loc를 사용하여 'Date' 열을 다시 처리합니다.
        df.loc[:, 'Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

        # 
        custom_strategy = ta.Strategy(
                        name="Momo and Volatility",
                        description="des",
                        ta=ta_custom_indicators
        )
        df.ta.strategy(custom_strategy)
        cdl_pattern_df = df.ta.cdl_pattern(name=ta_custom_patterns)
        df = pd.concat([df, cdl_pattern_df], axis=1)
        
        return df

  

    def ohlc_indicator(self):
        # Implement your OHLC indicator code here.
        pass
    def stock_eps(self,config_dict):
        self.stockticker.rename(columns={'종목코드': '티커'}, inplace=True)
        # dfkospi = stock.get_market_fundamental(timefunction("년월일"), market="KOSDAQ")
        # dfkosdaq = stock.get_market_fundamental(timefunction("년월일"), market="KOSPI")
        dfkospi = stock.get_market_fundamental("20230818", market="KOSDAQ")
        dfkosdaq = stock.get_market_fundamental("20230818", market="KOSPI")
        df = pd.concat([dfkospi, dfkosdaq], axis=0)
        df.reset_index(inplace=True)

        df.to_csv(f"{self.datasetspath}/eps.csv",index=False)
        
        df_filtered = df[df['EPS'] > config_dict['Stock_OHLC_Select']['EPS']]     
        df_filtered = df_filtered[
            ((df_filtered['BPS'] > config_dict['Stock_OHLC_Select']['BPS']) | (df_filtered['PBR'] > config_dict['Stock_OHLC_Select']['PBR'])) &
            ((df_filtered['PER'] < config_dict['Stock_OHLC_Select']['PER']) | (df_filtered['PER'] > 10) ) |
            ( df_filtered['DPS'] > config_dict['Stock_OHLC_Select']['DPS']) 
            
        ]
        # # EPS (Earnings Per Share):
        # df_filtered = df[df['EPS'] > config_dict['Stock_OHLC_Select']['EPS']]
        # # DPS (Dividends Per Share):
        # # DIV (Dividend Yield):
        # df_filtered = df_filtered[df_filtered['DPS'] > config_dict['Stock_OHLC_Select']['DPS']]
        # # PBR (Price-to-Book Ratio):
        # df_filtered = df_filtered[df_filtered['PBR'] > config_dict['Stock_OHLC_Select']['PBR']]
        # # PER (Price-to-Earnings Ratio):
        # df_filtered = df_filtered[df_filtered['PER'] > config_dict['Stock_OHLC_Select']['PER']]
        # # BPS (Book Value Per Share):
        # df_filtered = df_filtered[df_filtered['BPS'] > config_dict['Stock_OHLC_Select']['BPS']]

        result_inner = pd.merge(self.stockticker, df_filtered, on='티커', how='inner')
        
        result_inner[['티커','종목명','Market','BPS','PER','PBR','EPS','DIV','DPS','Stocks']].to_csv(f"{self.datasetspath}/df_filtered.csv",index=False)

        return result_inner[['티커','종목명','Market','BPS','PER','PBR','EPS','DIV','DPS','Stocks']]      
    def get_etf_index(self):
   
        coreDf=self.stock_eps(self.configdict )
        eftCodelist=stock.get_index_portfolio_deposit_file(self.ETFCODE)
   
        filtered_df = coreDf[coreDf['티커'].isin(eftCodelist)]
        eftCodelist = filtered_df['티커'].to_list()    
        print(len(eftCodelist),eftCodelist)



        cp_with_ca = [cp_item + f".{self.CATEGORY}" for cp_item in eftCodelist]
        # cp_with_ca.insert(0, "^KS11")
        # cp_with_ca.insert(0, "^KQ11")



        thn=len(cp_with_ca)-1

        cp_with_ca = cp_with_ca[0:thn]
        prGreen(f'{len(cp_with_ca)},{cp_with_ca}')


        return  cp_with_ca
    def fetch_ohlc(self,tickers):
    # try:
        # Fetch OHLC data from Yahoo Finance using the provided config_dict
        # tickers : str, list
        #     List of tickers to download
        # period : str
        #     Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        #     Either Use period parameter or use start and end
        # interval : str
        #     Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        #     Intraday data cannot extend last 60 days
    
        
        ohlc_config_list = self.configdict['Stock_OHLC_Select']
        # s = config_dict['Stock_OHLC_Select']['symbol']
        i=self.configdict['Stock_OHLC_Select']['interval']
        c=self.configdict['Stock_OHLC_Select']['count']
        st=self.configdict['Stock_OHLC_Select']['startdate']
        ed = self.configdict['Stock_OHLC_Select']['enddate']
        # df = pd.DataFrame()
        if i=='1d':
            # start date 빼버리면, 총얄
            df = yf.download(tickers ,interval=i, period='1y', auto_adjust=False,group_by='ticker')    
            # 코스닥 date_to_delete = '2022-12-26' 이날 yfinance 에 결측 있어서 값이 zero dive 생김
            # print(df)
            # 코스닥 만 이날짜에 삭제
            # date_to_delete = '2022-12-26'
            # df = df[df.index != date_to_delete]
        elif i=='5d':
            # start date 빼버리면, 총얄
            df = yf.download(tickers ,interval=i, period='2y', auto_adjust=False,group_by='ticker')    
            # 코스닥 date_to_delete = '2022-12-26' 이날 yfinance 에 결측 있어서 값이 zero dive 생김
            # 코스닥 만 이날짜에 삭제
            # date_to_delete = '2022-12-26'
            # df = df[df.index != date_to_delete]
        else:
            df = yf.download(tickers, start=st,interval=i, auto_adjust=False,group_by='ticker')
            df = df.dropna()
        # 인덱스 이름을 공통으로 전체 변경 안그러면 약간이상해짐 , 수행에는 문제 없으면 절대 필요
        df.index.name = 'Date'
        return df
               
    def main(self):
        # print(self.configdict)
        tickerlist = self.get_etf_index()
        
        results=self.fetch_ohlc(tickerlist)
        print(tickerlist)
        
        for ticker in tickerlist:

           
            df= results[ticker]
            t = ticker.split('.')[0] 
            
            print(t)
            df.to_csv(f'/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/datasets/koreadaily/{t}{self.CATEGORY}.csv', index=True)
         
       
        result_type = type(results)
        

        # print(results['066970.KQ'])
        # results.to_csv('/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/datasets/koreadaily/result.csv', index=False)
        # You can add code here to perform the main tasks of your program.
        # For example, you can create an instance of the class and call its methods.

if __name__ == "__main__":

    ticker_instance = GetTickerFromStock("KQ","2203")
    ticker_instance.main()

    # df = pd.read_csv("/Users/hg/DEV/WebDocuments/public/DailyInfo/stock/datasets/koreadaily/348370KQ.csv", index_col='Date')
    # # print(df)
    # # print(df.ta.log_return(cumulative=True, append=True)) 
    # # print(df.ta.percent_return(cumulative=True, append=True))
    # # print(df.tail())    

    # MyStrategy = ta.Strategy(
    # name="DCSMA10",
    # ta=[
    #     {"kind": "ohlc4"},
    #     {"kind": "sma", "length": 10},
    #     {"kind": "donchian", "lower_length": 10, "upper_length": 15},
    #     {"kind": "ema", "close": "OHLC4", "length": 10, "suffix": "OHLC4"},
    # ]
    # )
    # df.ta.strategy(MyStrategy)
    # print(df)

    # def combine_stats(pf: vbt.portfolio.base.Portfolio, ticker: str, strategy: str, mode: int = 0):
    #     header = pd.Series({
    #         "Run Time": ta.get_time(full=False, to_string=True),
    #         "Mode": "LIVE" if mode else "TEST",
    #         "Strategy": strategy,
    #         "Direction": vbt.settings.portfolio["signal_direction"],
    #         "Symbol": ticker.upper(),
    #         "Fees [%]": 100 * vbt.settings.portfolio["fees"],
    #         "Slippage [%]": 100 * vbt.settings.portfolio["slippage"],
    #         "Accumulate": vbt.settings.portfolio["accumulate"],
    #     })
    #     rstats = pf.returns_stats().dropna(axis=0).T
    #     stats = pf.stats().dropna(axis=0).T
    #     joint = pd.concat([header, stats, rstats])
    #     return joint[~joint.index.duplicated(keep="first")]

    # def earliest_common_index(d: dict):
    #     """Returns index of the earliest common index of all DataFrames in the dict"""
    #     min_date = None
    #     for df in d.values():
    #         if min_date is None:
    #             min_date = df.index[0]
    #         elif min_date < df.index[0]:
    #             min_date = df.index[0]
    #     return min_date

    # def dl(tickers: list, same_start: bool = False, **kwargs):
    #     if isinstance(tickers, str):
    #         tickers = [tickers]
        
    #     if not isinstance(tickers, list) or len(tickers) == 0:
    #         print("Must be a non-empty list of tickers or symbols")
    #         return

    #     if "limit" in kwargs and kwargs["limit"] and len(tickers) > kwargs["limit"]:
    #         from itertools import islice            
    #         tickers = list(islice(tickers, kwargs["limit"]))
    #         print(f"[!] Too many assets to compare. Using the first {kwargs['limit']}: {', '.join(tickers)}")

    #     print(f"[i] Downloading: {', '.join(tickers)}")

    #     received = {}
    #     start_date = "2023-01-01"
    #     end_date = "2023-10-01"
    #     if len(tickers):
    #         _df = pd.DataFrame()
    #         for ticker in tickers:
    #             received[ticker] = _df.ta.ticker(ticker,start=start_date, end=end_date)
    #             print(f"[+] {ticker}{received[ticker].shape} {ta.get_time(full=False, to_string=True)}")
        
    #     if same_start and len(tickers) > 1:
    #         earliestci = earliest_common_index(received)
    #         print(f"[i] Earliest Common Date: {earliestci}")
    #         result = {ticker:df[df.index > earliestci].copy() for ticker,df in received.items()}
    #     else:
    #         result = received
    #     print(f"[*] Download Complete\n")
    #     return result

    # def dtmask(df: pd.DataFrame, start: datetime, end: datetime):
    #     return df.loc[(df.index >= start) & (df.index <= end), :].copy()

    # def show_data(d: dict):
    #     [print(f"{t}[{df.index[0]} - {df.index[-1]}]: {df.shape} {df.ta.time_range:.2f} years") for t,df in d.items()]
        
    # def trade_table(pf: vbt.portfolio.base.Portfolio, k: int = 1, total_fees: bool = False):
    #     if not isinstance(pf, vbt.portfolio.base.Portfolio): return
    #     k = int(k) if isinstance(k, int) and k > 0 else 1

    #     df = pf.trades.records[["status", "direction", "size", "entry_price", "exit_price", "return", "pnl", "entry_fees", "exit_fees"]]
    #     if total_fees:
    #         df["total_fees"] = df["entry_fees"] + df["exit_fees"]

    #     print(f"\nLast {k} of {df.shape[0]} Trades\n{df.tail(k)}\n")

    # # start_date = "2023-01-01"
    # # end_date = "2023-10-01"

    # # # Fetch data for the given ticker within the specified period
    # # df = pd.DataFrame().ta.ticker("166090.KQ", start=start_date, end=end_date)


    # # df["GC"] = df.ta.sma(50, append=True) > df.ta.sma(50, append=True)

    # # # Create boolean Signals(TS_Entries, TS_Exits) for vectorbt
    # # golden = df.ta.tsignals(df.GC, asbool=True, append=True)

    # # # Sanity Check (Ensure data exists)
    # # print(df)






    # cheight, cwidth = 500, 1000 # Adjust as needed for Chart Height and Width
    # vbt.settings.set_theme("dark") # Options: "light" (Default), "dark" (my fav), "seaborn"

    # # Must be set
    # vbt.settings.portfolio["freq"] = "1D" # Daily

    # # Predefine vectorbt Portfolio settings
    # # vbt.settings.portfolio["init_cash"] = 100
    # vbt.settings.portfolio["fees"] = 0.0025 # 0.25%
    # vbt.settings.portfolio["slippage"] = 0.0025 # 0.25%
    # # vbt.settings.portfolio["size"] = 100
    # # vbt.settings.portfolio["accumulate"] = False
    # vbt.settings.portfolio["allow_partial"] = False

    # pf_settings = pd.DataFrame(vbt.settings.portfolio.items(), columns=["Option", "Value"])
    # pf_settings.set_index("Option", inplace=True)

    # print(f"Portfolio Settings [Initial]")
    # print(pf_settings)
    # # # # Create the Signals Portfolio
    # # pf = vbt.Portfolio.from_signals(df.Close, entries=golden.TS_Entries, exits=golden.TS_Exits, freq="D", init_cash=100_000, fees=0.0025, slippage=0.0025)

    # # # Print Portfolio Stats and Return Stats
    # # print(pf.stats())
    # # print(pf.returns_stats())


    # benchmark_tickers = ["003380.KQ", "287410.KQ"]
    # asset_tickers = ["131290.KQ", "140860.KQ"]
    # all_tickers = benchmark_tickers + asset_tickers

    # print("Tickers by index #")
    # print("="*100)
    # print(f"Benchmarks: {', '.join([f'{k}: {v}' for k,v in enumerate(benchmark_tickers)])}")
    # print(f"    Assets: {', '.join([f'{k}: {v}' for k,v in enumerate(asset_tickers)])}")
    # print(f"       All: {', '.join([f'{k}: {v}' for k,v in enumerate(all_tickers)])}")

    # benchmark = benchmark_tickers[0] # Change index for different benchmark
    # asset = asset_tickers[1] # Change index for different symbol
    # print(f"Selected Benchmark | Asset: {benchmark} | {asset}")
    # benchmarks = dl(benchmark_tickers, lc_cols=True)
    # assets = dl(asset_tickers, lc_cols=True)


    # start_date = "2021-01-01"
    # end_date = "2023-10-13"

    # # start_date = datetime(2023, 1, 1) # Adjust as needed
    # # end_date = datetime(2023, 10, 1)   # Adjust as needed
    # benchmark_name = "003380.KQ" # Select a Benchmark
    # asset_name = "140860.KQ" # Select an Asset

    # benchmarkdf = benchmarks[benchmark_name]
    # assetdf     = assets[asset_name]

    # # Set True if you want to constrain Data between start_date & end_date
    # common_range = True
    # if common_range:
    #     crs = f" from {start_date} to {end_date}"
    #     benchmarkdf = dtmask(benchmarkdf, start_date, end_date)
    #     assetdf = dtmask(assetdf, start_date, end_date)

    # # Update DataFrame names
    # benchmarkdf.name = benchmark_name
    # assetdf.name = asset_name
    # print(f"Analysis of: {benchmarkdf.name} and {assetdf.name}{crs if common_range else ''}")



    # def trends(df: pd.DataFrame, mamode: str = "sma", fast: int = 4, slow: int = 57):
    #     return ta.ma(mamode, df.Close, length=fast) < ta.ma(mamode, df.Close, length=slow) 
    # trend_kwargs = {"mamode": "sma", "fast": 4, "slow": 46}

    # benchmark_trends = trends(benchmarkdf, trend_kwargs)
    # benchmark_trends.copy().astype(int).plot(figsize=(16, 1), kind="area", color=["green"], alpha=0.45, title=f"{benchmarkdf.name} Trends", grid=True)

    # asset_trends = trends(assetdf, trend_kwargs)
    # asset_trends.copy().astype(int).plot(figsize=(16, 1), kind="area", color=["green"], alpha=0.45, title=f"{assetdf.name} Trends", grid=True)



    # # trade_offset = 0 for Live Signals (close is last price)
    # # trade_offset = 1 for Backtesting
    # LIVE = 0

    # benchmark_signals = assetdf.ta.tsignals(benchmark_trends, asbool=True, trade_offset=LIVE, append=True)
    # print(benchmark_signals.tail())


    # asset_signals = assetdf.ta.tsignals(asset_trends, asbool=True, trade_offset=LIVE, append=True)
    # asset_signals.tail()



    # benchmarkpf_bnh = vbt.Portfolio.from_holding(benchmarkdf.Close)
    # print(trade_table(benchmarkpf_bnh))
    # combine_stats(benchmarkpf_bnh, benchmarkdf.name, "Buy and Hold", LIVE)


    #     # Asset Buy and Hold (BnH) Strategy
    # assetpf_bnh = vbt.Portfolio.from_holding(assetdf.Close)
    # print(trade_table(assetpf_bnh))
    # combine_stats(assetpf_bnh, assetdf.name, "Buy and Hold", LIVE)



    # benchmarkpf_signals = vbt.Portfolio.from_signals(
    # benchmarkdf.Close,
    # entries=benchmark_signals.TS_Entries,
    # exits=benchmark_signals.TS_Exits,
    # )
    # trade_table(benchmarkpf_signals, k=5)
    # combine_stats(benchmarkpf_signals, benchmarkdf.name, "Long Strategy", LIVE)


    # # Asset Portfolio from Trade Signals
    # assetpf_signals = vbt.Portfolio.from_signals(
    #     assetdf.Close,
    #     entries=asset_signals.TS_Entries,
    #     exits=asset_signals.TS_Exits,
    # )
    # trade_table(assetpf_signals, k=5)
    # combine_stats(assetpf_signals, assetdf.name, "Long Strategy", LIVE)

    # vbt.settings.set_theme("seaborn")
    # benchmarkpf_signals.trades.plot(title=f"{benchmarkdf.name} | Trades", height=cheight, width=cwidth).show()
    # benchmarkpf_signals.value().vbt.plot(title=f"{assetdf.name} | Equity Curve", trace_kwargs=dict(name=u"\u00A4"), height=cheight // 2, width=cwidth).show()