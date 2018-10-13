"""
            Question:
            1. Will there be empty input?
            2. Will there be negative numbers?

            Idea:
            1. iterate from 1 to n
            2. sumation all prices[i+1] - prices[i] > 0

        """

prices = [7,1,5,3,6,4]

if len(prices) > 0:
    previous = prices[0]
    profit_sum = 0

    for price in prices:
        if price - previous > 0:
            profit_sum += price - previous
        previous = price
    print(profit_sum)
else:
    print(0)