import yfinance as yf


def get_ticker_info(ticker):
    ticker = yf.Ticker(ticker)
    return ticker.info
