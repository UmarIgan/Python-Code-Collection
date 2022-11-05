import pandas as pd
import datetime as dt
from ta import add_all_ta_features
import warnings
import json
import ppscore as pps
import io
import numpy as np
from datetime import date, timedelta

import requests

warnings.filterwarnings("ignore")
#pd.options.mode.chained_assignment = None
#pd.set_option('display.max_columns', None)
#pd.options.mode.chained_assignment = None

def get_response(url):
    response = requests.get(url)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()

def get_exchange_info():
    base_url = 'https://api.binance.com'
    endpoint = '/api/v3/exchangeInfo'
    return get_response(base_url + endpoint)
  
#creating list of binance assests
def create_symbols_list(filter='USDT'):
    rows = []
    info = get_exchange_info()
    pairs_data = info['symbols']
    full_data_dic = {s['symbol']: s for s in pairs_data if filter in s['symbol']}
    data = pd.DataFrame(pairs_data)
    data2 = data.loc[data['quoteAsset']=='USDT'].loc[data['status']=='TRADING']
    return list(data2['symbol'].values)

#main function to return an assests ohlc data
def get_bars (symbol, interval='1d'):
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads (requests.get (url).text)
    df = pd.DataFrame (data)
    df.columns = ['open_time',
                  'open', 'high', 'low', 'close', 'volume',
                  'close_time', 'qav', 'num_trades',
                  'buyer_seller_volume', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp (x / 1000.0) for x in df.open_time]
    df['close'] = pd.to_numeric (df['close'])
    df['open'] = pd.to_numeric (df['open'])
    df['high'] = pd.to_numeric (df['high'])
    df['low'] = pd.to_numeric (df['low'])
    df['volume'] = pd.to_numeric (df['volume'])
    df['close'] = pd.to_numeric (df['close'])
    df['buyer_seller_volume'] = pd.to_numeric (df['buyer_seller_volume'])
    df['num_trades'] = pd.to_numeric (df['num_trades'])
    df['symbol'] = symbol
    df = df.drop(['close_time', 'open_time'], axis=1)
    #df_.loc[:, 'name'] = symbol
    return df


#function to return assests ohlc data for multiple crypto
def return_data(symbols, interval='1h'):
    if type(symbols) == list:
        symbols = symbols
    else:
        symbols = [symbols]
    listi = []
    for i in symbols:
        data = get_bars (i, interval=interval)
        listi.append (data)
    dfi = pd.concat ([pd.DataFrame (x) for x in listi]).apply (pd.Series)
    return dfi

def return_close_values(symbols, interval='1h'):
    if type(symbols) == list:
        symbols = symbols
    else:
        symbols = [symbols]
    listi = []
    for i in symbols:
        data = get_bars (i, interval=interval)
        data['symbol'] = i
        listi.append (data)
    dfi = pd.concat ([pd.DataFrame (x) for x in listi]).apply (pd.Series)
    lis = dfi[['close', 'symbol']].reset_index()
    data2 = lis.pivot_table(index='index', columns='symbol', values='close').reset_index ().rename_axis (None,axis=1).set_index ('index').dropna ()
    data2.index = pd.to_datetime (data2.index)
    return data2

  
#function to return desired columns including indicators
def return_desired_data(column, symbols, interval='1h'):
    if type(symbols) == list:
        symbols = symbols
    else:
        symbols = [symbols]
    listi = []
    for i in symbols:
        data = get_bars(i, interval=interval)
        listi.append(data)
    data = pd.concat([pd.DataFrame(x) for x in listi]).apply(pd.Series)
    new_l = []
    for i in data['symbol'].unique():
        df_i = add_all_ta_features(data.loc[data['symbol'] == i], 'open', 'high', 'low', 'close', 'volume',
                                   fillna=False).drop('symbol', axis=1)
        df_i['symbol'] = i
        new_l.append(df_i)
    df_new = pd.concat(new_l)  # trend_psar_up, trend_psar_down,trend_stc,trend_mass_index,trend_trix
    df_new = df_new.drop(['trend_psar_up', 'trend_psar_down', 'trend_stc', 'trend_mass_index', 'trend_trix'],
                         axis=1).dropna()

    lis = df_new[[column, 'symbol']].reset_index()
    data2 = lis.pivot_table(index='index', columns='symbol', values=column).reset_index().rename_axis(None,
                                                                                                      axis=1).set_index(
        'index').dropna()
    data2.index = pd.to_datetime(data2.index)
    data2['date'] = data2.index
    return data2

#function to return an assest data with indicators
def return_data_with_indicator(symbols, interval='1h'):

    data = get_bars (symbols, interval=interval)

    df_i = add_all_ta_features (data, 'open', 'high', 'low', 'close', 'volume', fillna=False).drop('symbol', axis=1)
    df_i['symbol'] = symbols

    df_new=df_i.drop(['trend_psar_up', 'trend_psar_down','trend_stc','trend_mass_index','trend_trix',
                      'open', 'high','low', 'volume'],axis=1).dropna()

    best_ft = to_best_features (df_new)

    used_cols = list (best_ft.keys())


    return df_new[used_cols]
