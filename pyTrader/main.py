import constants.indexes as ind
import constants.convertion_ratio as ratio
import tools.ticker as tk
import tools.conversion as conv


def main():
    info = tk.get_ticker_info(ind.US_100)
    current = conv.get_stock_from_ratio(info['regularMarketPrice'], ratio.US100_YAHOO_XTB)

    print(current)


if __name__ == "__main__":
    main()
