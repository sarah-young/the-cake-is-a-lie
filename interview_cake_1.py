"""Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# Returns 6 (buying for $5 and selling for $11)"""

def best_profit(stock_prices_yesterday):
    """Take a list containing yesterday's stock prices.
    Return the best profit you could make from one sale."""

    max_profit = None
    min_price = stock_prices_yesterday[0]

    for current_price in stock_prices_yesterday:
        min_price = min(min_price, current_price)

        profit = current_price - min_price

        max_profit = max(max_profit, profit)

    return max_profit



    # First attempt
    # max_value = None
    # for i in range(len(stock_prices_yesterday[:-1])):
    #     print "i: ", stock_prices_yesterday[i]
    #     for j in range(len(stock_prices_yesterday[i:])):
    #         print "j: ", stock_prices_yesterday[j]
    #         delta = stock_prices_yesterday[j+i] - stock_prices_yesterday[i]
    #         print delta
    #         if delta > max_value:
    #             max_value = delta
    #             print max_value
    # return max_value


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

money = best_profit(stock_prices_yesterday)

print money
