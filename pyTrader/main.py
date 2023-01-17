import constants.indexes as ind
import constants.conversion_ratio as ratio
import tools.ticker as tk
import tools.conversion as conv


def main():
    # current = conv.get_stock_from_ratio(tk.get_current_value(ind.US_100), ratio.US100_YAHOO_XTB)
    # print(current)
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    df = tk.get_ticker_data(ind.US_100, '3mo', '1h')
    # print(df)
    levels = tk.detect_level_method_1(df)
    tk.plot_all(levels, df)


if __name__ == "__main__":
    main()
