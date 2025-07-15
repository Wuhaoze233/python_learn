'''
股票筛选 Stock dictionary

Author: Haoze Wu
Version: 1.0
'''

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stock2 = {key:value for key, value in stocks.items() if stocks[key] > 100}
print(stock2)