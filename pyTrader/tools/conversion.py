def get_stock_from_ratio(value, conversion_ratio):
    if conversion_ratio < 1:
        res = value / conversion_ratio
    else:
        res = value * conversion_ratio
    return round(res, 2)


