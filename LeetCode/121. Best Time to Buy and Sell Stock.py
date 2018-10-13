"""
        Question:
        1. Will there be negative value?
        2. How largest would the price can be?

        Idea:
        1. Use dynamic program
"""

prices = [7,1,5,3,6,4]

maxDiff = 0
lowest = float('inf')

for price in prices:
    lowest = min(lowest, price)
    maxDiff = max(maxDiff, price - lowest)

print(maxDiff)
