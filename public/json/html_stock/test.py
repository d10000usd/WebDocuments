import json
import pandas as pd


def read_json(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        return json.load(file)

jsons = read_json("/Users/hg/DEV/WebDocuments/public/json/html_stock/strategies_good_pattern.json")
print(jsons['^KQ11'])