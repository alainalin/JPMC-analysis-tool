import os
import json
import datetime 
import pandas as pd
import numpy as np
import yfinance as yf

# adjust these dates to pick a week of particular interest
# scale up later 
start_date = '2024-08-20'
end_date = '2024-08-28'

data_path = '/data/'

# get companies and corresponding stock symbols in S&P500 
company_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S%26P_500_component_stocks')[0]
stock_symbols = list(company_data.Symbol.values).append('SPY')
stock_symbols.sort()

# get stock data and store the dataframes for companies into individual csv files 
success_download = 0
for symbol in stock_symbols:
    try:
        df = yf.download(symbol, start=start_date, end=end_date)
        df = df[['Adj Close', 'Volume']]
        df.to_csv(os.path.join(data_path, '{}.csv'.format(symbol)))
        success_download += 1
    except KeyError:
        print('Error for {}'.format(symbol))
        pass
print('Successfully stored {}/{} files'.format(success_download, len(stock_symbols)))


