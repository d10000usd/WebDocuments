
import json

import time
import pandas as pd
import pyupbit
import requests



# from streamlit_gallery import apps, components
# from streamlit_gallery.utils.page import page_group

#namming rule
#common_ {from get data} function
#util_ {internal function}

tstamp = time.strftime('%Y%m%d', time.localtime(time.time()))




CurrentPath = "/Users/hg/PROJECT/frontend/hg-project-bootstrap/src/assets/coinInfo"
def common_get_allticker_today_changerate(ea,cointicker,rating):
# def common_get_allticker_today_changerate(ea,cointicker,rating=[-99,99]):
    ## 업비트 잔고 조회
    ## 업티트 잔고를 무조건 조회화면에 띄워줌
    ## getUPbitBalance() return 잔고정보전체를 가지고 있는 딕셔너리
    dictTodataframeToJsonfile(getUPbitBalance(),f"{CurrentPath}","balance")


    # """업비트 티커 조회
    # Index(['market', 'trade_date', 'trade_time', 'trade_date_kst',
    #    'trade_time_kst', 'trade_timestamp', 'opening_price', 'high_price',
    #    'low_price', 'trade_price', 'prev_closing_price', 'change',
    #    'change_price', 'change_rate', 'signed_change_price',
    #    'signed_change_rate', 'trade_volume', 'acc_trade_price',
    #    'acc_trade_price_24h', 'acc_trade_volume', 'acc_trade_volume_24h',
    #    'highest_52_week_price', 'highest_52_week_date', 'lowest_52_week_price',
    #    'lowest_52_week_date', 'timestamp'],
    #   dtype='object')
    # """
    url = "https://api.upbit.com/v1/ticker"
    params = {"markets": cointicker}
    res = requests.get(url, params=params,timeout=10)
    data = res.json()
    #데이터값 변경 없비트 티커포맷  - > 변경
    td=pd.DataFrame(data)

 




    td['signed_change_rate']=round(td['signed_change_rate']*100,3)
    td=td.sort_values(by='signed_change_rate' ,ascending=False).reset_index()## 10~1 순서로 상승률 내림차순
    #td=td.where((td['signed_change_rate'] == '0') & (df['A'] == 20))
    
    #rating = [-2,3] bottom, top
    td=td[td['signed_change_rate']  >rating[0] ] #상승률이 -2% 이상인것만
    td=td[td['signed_change_rate']  <rating[1] ] #상승률이 3% 이하인것만
    print("updated coin info")
    print(ea)
    # rank 순위 8개만 목록을 만들고

    delistingcoin = [
    "KRW-KRW",

    "KRW-USDT",
    "KRW-VTHO",
    "KRW-LUNC",
    "KRW-LUNA2",
    "KRW-APENFT",
    "KRW-BTT",
    "KRW-DON",

        ]
    td = td.drop(td[td["market"].isin(delistingcoin)].index)

    # (td['market'].head(int(ea))).to_json(f'{CurrentPath}/tickers_rating_order.json',indent=4, orient='records',force_ascii=False)
    
    # Rank 를 구해서
    # BTT 제거후 리스트타입으로 삭제 가능
    td = td[~td.isin(["KRW-BTT"])]
    td = td[td['market'].isin(white_list())]  # white list
    #td = (td[~td.isin(black_list())]) #black list
 
    td['market'].to_json(f'{CurrentPath}/tickers.json',indent=4, orient='records',force_ascii=False)
    # if(1):# 백테스트할때 pairlist.json 파일에 코인 추가
    #     util_list_to_jsonfile(f"/Users/hg/WORKSPACE/.command/pairs_Allcoin.json",td['market'].tolist())
    #     util_list_to_jsonfile(f"/Users/hg/WORKSPACE/MONEY/upbit_ft_userdata_real_trade/user_data/data/upbit/pairs_Allcoin.json",td['market'].tolist())
    return td.to_dict()
def dataframe_find_row_value_change(df,changevalue):
    df=df[df['signed_change_rate']  >changevalue ] #상승률이 -2% 이상인것만
    return df

def white_list():
    basic_white_list=get_basic_white_list()
    today_white_list=get_today_white_list()
    balance_list=get_balanceCoin_list()
    
    white_lists=get_monitoring_list()
    white_lists.extend(today_white_list)
    white_lists.extend(basic_white_list)
    white_lists.extend(balance_list)
  
    # white_lists=pyupbit.get_tickers(fiat="KRW")
    return white_lists
def get_today_white_list():
    today_white_list=["KRW-SRM"]
    return today_white_list
def get_basic_white_list():
    basic_white_list=["KRW-BTC","KRW-ETH"]
    return basic_white_list

def get_monitoring_list():
    # column_names = ['watchlist']
    df = pd.read_json(f"{CurrentPath}/tickers_watch.json")

    df = df.rename(columns={0: 'watchlist'})
    
 
    return df['watchlist'].to_list()

def get_balanceCoin_list():
    #jsonfileread dataframe 
    path_=f"{CurrentPath}/balance_info.json"
    df = pd.read_json(path_, orient='records',encoding='utf-8')
    
    balanceCoin_list=df["cointicker"].to_list()
   
    return balanceCoin_list
def black_list():
    black_lists=["KRW-ETH"]
    return black_lists
def get_upbit_ticker():
    tickers = pyupbit.get_tickers(fiat="KRW")
    return tickers

def coin_config_json_1():
    stock_contents_article =[
            {'tickers' : get_upbit_ticker()},  
            {'whitelist' : white_list()},
            {'blacklist': black_list()},
            {'up': -5},
            {'down': 1},
            {'sort': 'assending'},
            {'time': 0}]
    return stock_contents_article
    

def dictTodataframeToJsonfile(dictionaryd,savepath,fname): #특수문자가 깨져서 따로 만들어줌
    path = f"{savepath}/{fname}.json"

    df = pd.DataFrame([dictionaryd])
    json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=4)
    parsed = json.loads(json_1)

    with open(path, 'w',encoding="utf-8") as json_file:
        json_file.write(json.dumps(parsed, indent=4, ensure_ascii=False,))
        # json_file.write(json.dumps({"fulldata": parsed}, indent=4, ensure_ascii=False,))
#rating = [-2,3] 
# coin price change rate at today
# common_get_allticker_today_changerate(get_upbit_ticker(),rating=[-11,311,]) # type: ignore

# 
def getUPbitBalance():
    accessKey =  "AELrhn9P8niOr6nMby0n8MsvcjaV6fvAmfJXZF7z"
    secretKey =  "hIPEUQFOY9RxUIa1rsxWuzuK2oHKDww806SLJU5U"
    upbit = pyupbit.Upbit(accessKey, secretKey)
    balance = upbit.get_balances()       # 보유 현금 조회


    df = pd.DataFrame(balance)

    df["cointicker"]=df["unit_currency"]+"-"+df["currency"]
    #잔고정보중 코인티커만 저장



    delistingcoin = [
    "KRW-KRW",

    "KRW-USDT",

    "KRW-VTHO",
    "KRW-LUNC",

    "KRW-LUNA2",
    "KRW-APENFT",
    "KRW-BTT",
    "KRW-DON",

        ]
    df = df.drop(df[df["cointicker"].isin(delistingcoin)].index)
    df["cointicker"].to_json(  f'{CurrentPath}/balance_ticker.json',indent=4, orient='records',force_ascii=False)
    #잔고정보전체를 저장
    df.to_json(  f'{CurrentPath}/balance_info.json',indent=4, orient='records',force_ascii=False)
   
    return balance

def rating_coin_order(orderCount):
    res=common_get_allticker_today_changerate(orderCount,get_upbit_ticker(),rating=[-11,311,])
   
    return res # type: ignore


def getTicker():
    res=pyupbit.get_tickers("KRW")
    
    df = pd.DataFrame(res, columns=['watchlist'])
    df['name'] =  df['watchlist']
    print(df)
    df['watchlist'].to_json(  f'{CurrentPath}/tickers.json',indent=4, orient='records',force_ascii=False)
    df.to_csv(  f'{CurrentPath}/tickers.csv', index=False,header=False,encoding='utf-8-sig')
    return df.to_dict()


def getOrderBook():
    res = pyupbit.get_orderbook("KRW-BTC")
   
    return res
if __name__ == "__main__":

    rating_coin_order(150)