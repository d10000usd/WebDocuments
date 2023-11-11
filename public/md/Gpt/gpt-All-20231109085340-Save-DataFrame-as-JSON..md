# **<span style="font-size: 35px; font-style: italic;">Save DataFrame as JSON.</span>**

## Description




<div style="display: flex; align-items: center; font-size: 16px;"><div><img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-34.png" width="50" height="50" style="vertical-align: middle;" /></div><div style="display: inline-block; vertical-align: middle; margin-left: 10px; font-size: 16px;">Context 4</div></div>
To save the dataframe as a JSON file, you can use the following code. Make sure you have the necessary libraries, such as pandas, installed before running this code:

```python
import pandas as pd

# Sample DataFrame
data = {'Start': ['2022-11-08 00:00:00'],
        'End': ['2023-11-08 00:00:00'],
        'Duration': ['365 days 00:00:00'],
        'Exposure Time [%]': [89.878543],
        'Equity Final [$]': [47544724.372969],
        'Equity Peak [$]': [68717650.372969],
        'Return [%]': [375.447244],
        'Buy & Hold Return [%]': [464.813985],
        'Return (Ann.) [%]': [390.691866],
        'Volatility (Ann.) [%]': [555.39518],
        'Sharpe Ratio': [0.703448],
        'Sortino Ratio': [7.220867],
        'Calmar Ratio': [8.588554],
        'Max. Drawdown [%]': [-45.489831],
        'Avg. Drawdown [%]': [-11.614097],
        'Max. Drawdown Duration': ['106 days 00:00:00'],
        'Avg. Drawdown Duration': ['22 days 00:00:00'],
        '# Trades': [7],
        'ticker': ['에코프로'],
        'explain': ['# Explain 에코프로']}

df = pd.DataFrame(data)

# Save as JSON
df.to_json('data.json', orient='records', lines=True)
```

This code will save the dataframe as a JSON file named 'data.json' in the current working directory. Adjust the DataFrame creation part with your actual data before running the code.



<div style="background-color: grey; height: 15px;"></div>







<div style="background-color: grey; ">  

## meta   
![ex_screenshot](https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-31.png)  
* Save DataFrame as JSON.  
* 20231109085340  
* Description for dev  
* #keyword  
****
Drawdown [%]': [-45.489831],
        'Avg  
</div> 
