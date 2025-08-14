import requests as rs
import pandas as pd
import json


#Funkcje do śledzenia cen tokenów i do wyciągania parametrów :)
def get_pools_info(query):
    res = rs.get(f'https://api.geckoterminal.com/api/v2/search/pools?query={query}&page=1')
    res_json = json.loads(res.text)
    return res_json['data']

def get_pools_address(json_data):
    for i in range(len(json_data)):
        return json_data[i]['attributes']['address'] if i == 0 else 'Not supported index!!!'


# print(get_pools_info('redo'))
# print(get_pools_address(get_pools_info('redo')))

#Wyciągnięcie cen zamknięć do wykonania analizy technicznej i sprawdzenia patterów świec (zobaczymy co da się zrobić :))

def get_ohlcvs_of_pool(pool_addr, network, timeframe):
    ohlcvs = rs.get(f'https://api.geckoterminal.com/api/v2/networks/{network}/pools/{pool_addr}/ohlcv/{timeframe}?limit=1000')
    ohlcvs_json = json.loads(ohlcvs.text)
    raw = ohlcvs_json['data']['attributes']['ohlcv_list']
    df = pd.DataFrame(raw, columns=["Timestamp", "Open", "High", "Low", "Close", "Volume"])
    return df

# print(get_ohlcvs_of_pool(get_pools_address(get_pools_info('redo')), 'ton', 'day'))