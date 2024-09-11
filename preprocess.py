import os
import json
import datetime 
import pandas as pd
import numpy as np
import yfinance as yf

pd.options.mode.chained_assignment = None  # default='warn'

def getSymbols() -> list[str]:
    '''
    get companies and corresponding stock symbols in S&P500 
    '''
    company_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S%26P_500_component_stocks')[0]
    stock_symbols = list(company_data.Symbol.values)
    stock_symbols.append('SPY')
    stock_symbols.sort()
    return stock_symbols

def downloadData(data_dir, start_date: str, end_date: str, cols: list[str], symbols: list[str]) -> tuple[list[pd.DataFrame], list[str]]:
    '''
    data_dir :: data directory relative to this file 
    start_date :: YYYY-MM-DD inclusive
    end_date :: YYYY-MM-DD exclusive 
    cols :: attributes of interst that we want to retain in stored dataframes 
    symbols :: company stock symbols of interest 

    download stock data for the specified companies and store resulting dataframes

    return a list of the downloaded dataframes and a list of symbols of failed downloads 
    '''
    dataframes = []
    failed_downloads = []
    success_downloads = 0

    for symbol in symbols:
        try: 
            df = yf.download(symbol, start=start_date, end=end_date)

            if df.empty:
                failed_downloads.append(symbol)
                print('Failed to download {} data'.format(symbol))
                continue 

            df = df[cols]
            df.to_csv(os.path.join(data_dir, "{}.csv".format(symbol)))

            df.loc[:, 'Company'] = symbol
            dataframes.append(df)

            success_downloads += 1
        except KeyError:
            print('Error for symbol {}'.format(symbol))
            pass
    
    print('\nSuccessfully downloaded {}/{} files'.format(success_downloads, len(symbols)))
    return dataframes, failed_downloads

def loadData(data_dir: str, symbols: list[str]) -> list[pd.DataFrame]:
    '''
    data_dir :: data directory relative to this file 
    symbols :: company stock symbols of interest 

    return a list of the downloaded dataframes
    '''
    dataframes = []
    for symbol in symbols:
        df = pd.read_csv(os.path.join(data_dir, symbol+".csv")).set_index('Date')
        df.index = pd.to_datetime(df.index)
        df.loc[:, 'Company'] = symbol # retain company info 

        dataframes.append(df)

    return dataframes

def aggregateAndPreprocess(data_dir:str, start_date: str, end_date: str, symbols: list[str], dataframes: list[pd.DataFrame]):
    '''
    data_dir :: data directory relative to this file 
    start_date :: YYYY-MM-DD inclusive
    end_date :: YYYY-MM-DD exclusive 
    symbols :: company stock symbols of interest 
    dataframes :: list of dataframes corresponding to symbols, start_date, end_date
    '''
    # initialize empty dataframes 
    index = pd.date_range(start=start_date, end=end_date, freq='D')     # initialize an empty DateTime Index
    df_acprice = pd.DataFrame(index=index, columns=symbols)         # initialize empty dataframes
    df_volume = pd.DataFrame(index=index, columns=symbols)

    # aggregate all stock symbols into a price dataframe and volume dataframe
    # expects each df in dataframes to have a 'Company' column with the company stock symbol corresponding to its data
    for df in dataframes:
        company = df['Company'].iloc[0]

        df_acprice[company] = df['Adj Close']
        df_volume[company] = df['Volume']

    # masterDF = pd.concat(dataframes)

    # drop the dates where all the stocks are NaNs
    # ie. weekends/holidays where no trading occured
    df_acprice.dropna(how='all', inplace=True)
    df_volume.dropna(how='all', inplace=True)
    df_acprice.dropna(inplace=True, axis=1)
    df_volume.dropna(inplace=True, axis=1)
    assert((df_acprice.index == df_volume.index).all())

    df_acprice.to_csv(os.path.join(data_dir, "adj-closing-prices.csv"), index_label='date')
    df_volume.to_csv(os.path.join(data_dir, "volume.csv"))

def main():
    # adjust these dates to pick a week of particular interest
    # scale up later 
    start_date = '2024-08-20'
    end_date = '2024-08-28'

    data_dir = 'data/'
    columns = ['Adj Close', 'Volume']

    symbols = getSymbols()
    dataframes, failedSym = downloadData(data_dir, start_date, end_date, columns, symbols)
    aggregateAndPreprocess(data_dir, start_date, end_date, symbols, dataframes)
