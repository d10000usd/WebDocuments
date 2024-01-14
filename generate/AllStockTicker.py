import json
import FinanceDataReader as fdr


# Get the list of all stocks from KRX
df_krx = fdr.StockListing('KRX')

# Map the market names to the desired format
market_mapping = {'KOSPI': 'KS', 'KOSDAQ': 'KQ', 'KOSDAQ GLOBAL': 'KQ'}
df_krx['Market'] = df_krx['Market'].map(market_mapping)

# Filter the DataFrame based on the modified 'Market' column
filtered_df = df_krx[df_krx['Market'].isin(['KS', 'KQ'])]

# Select the 'Name', 'Code', and 'Market' columns
selected_columns = ['Name', 'Code', 'Market']
filtered_df = filtered_df[selected_columns]

# Exclude entries where the key contains '스팩'
filtered_df = filtered_df[~filtered_df['Name'].str.contains('스팩')]

# Create a dictionary in the desired format
filtered_dict = {name: [market,name,code] for name, code, market in zip(filtered_df['Name'], filtered_df['Code'], filtered_df['Market'])}

# Write the dictionary to a JSON file


with open('/Users/hg/PROJECT/frontend/hg-project-bootstrap/src/assets/stock/json/AllStockTicker_korname.json', 'w', encoding='utf-8') as json_file:
    json.dump(filtered_dict, json_file, indent=2, ensure_ascii=False)