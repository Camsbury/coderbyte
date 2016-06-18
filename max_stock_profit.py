# -*- coding: utf-8 -*-
"""
Max stock profit problem
"""

def max_stock_profit(prices):
    profit = [0]
    buy = sell = prices[0]
    for i in prices[1:]:
        if i > sell:
            sell = i
            profit[-1] = sell-buy
        if i < buy:
            buy = i
            sell = i
            profit.append(0)
    return max(profit)