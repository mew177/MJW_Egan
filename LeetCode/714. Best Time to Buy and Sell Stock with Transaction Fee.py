"""
            Question:
            1. Suppose there is not going to have negative fee
            2. Suppose there is not going to have negative price

            Idea:
            1. Dynamic programming
            2. In each state, either having a stock or not
            3. either you buy or sell to become the state of having stock or not
            4. memoization

        """

prices = [1, 3, 2, 4, 8, 4, 9]
fee = 2

noStock, hasStock = 0, -float("inf")

for i in range(0, len(prices)):
    # if you don't have stock today,
    # (1) you're not having a stock the previous day, you may not want to buy today either
    # (2) you're having a stock the previous day, you sell it today
    noStock = max(noStock, hasStock + prices[i] - fee)

    # if you have stock today,
    # (1) you're having a stock the previous day, you may want to keep it today either
    # (2) you're not having a stock the previous day, you buy it today
    hasStock = max(hasStock, noStock - prices[i])
print(noStock)