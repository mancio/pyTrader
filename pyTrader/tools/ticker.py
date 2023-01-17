import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.dates as mpl_dates
from matplotlib import pyplot as plt
import mplfinance as mpf


def get_ticker_info(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.info


def get_current_value(ticker):
    return get_ticker_info(ticker)['regularMarketPrice']


def get_ticker_data(symbol, period, interval):
    return yf.download(symbol, interval=interval, period=period, threads=False)


def get_stock_price_table(symbol, period, interval):
    df = get_ticker_data(symbol, period, interval)
    df['Date'] = pd.to_datetime(df.index)
    df['Date'] = df['Date'].apply(mpl_dates.date2num)
    df = df.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    return df


def plot_all(levels, df):
    s = mpf.make_mpf_style(base_mpf_style='default', y_on_right=True)
    mpf.plot(df, type='candle',
             hlines=dict(hlines=levels, linestyle='-.', colors=['r'], linewidths=(1, 1)),
             tight_layout=False, figratio=(15, 5), style=s)


def is_support(df, i):
    cond1 = df['Low'][i] < df['Low'][i - 1]
    cond2 = df['Low'][i] < df['Low'][i + 1]
    cond3 = df['Low'][i + 1] < df['Low'][i + 2]
    cond4 = df['Low'][i - 1] < df['Low'][i - 2]
    return cond1 and cond2 and cond3 and cond4


# determine bearish fractal
def is_resistance(df, i):
    cond1 = df['High'][i] > df['High'][i - 1]
    cond2 = df['High'][i] > df['High'][i + 1]
    cond3 = df['High'][i + 1] > df['High'][i + 2]
    cond4 = df['High'][i - 1] > df['High'][i - 2]
    return cond1 and cond2 and cond3 and cond4


# to make sure the new level area does not exist already
def is_far_from_level(value, levels, df):
    ave = np.mean(df['High'] - df['Low'])
    return np.sum([abs(value - level) < ave for _, level in levels]) == 0


def detect_level_method_1(df):
    levels = []
    for i in range(2, df.shape[0] - 2):
        if is_support(df, i):
            l = df['Low'][i]
            if is_far_from_level(l, levels, df):
                levels.append((i, l))
        elif is_resistance(df, i):
            l = df['High'][i]
            if is_far_from_level(l, levels, df):
                levels.append((i, l))
    return get_support_resistance_values(levels)


def get_support_resistance_values(levels):
    second_numbers = []
    for couple in levels:
        second_numbers.append(couple[1])
    return second_numbers
