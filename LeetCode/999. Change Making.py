"""
    Problem Description:

    Coin set = {x1, x2, x3,..., xn}
    Value = L

    Output1: Is there a subset of coins that sums to L?
    Output2: Subset of coins that sums to L if it's possible

"""

coins = [1, 3, 3]

def changeMaking(coins, L):
    if len(coins) == 1:
        if coins[0] == L:
            return True
        else:
            return False
    elif L < 0:
        return False
    else:
        return changeMaking( changeMaking(coins[:len(coins)-1], L) or changeMaking(coins[:len(coins)-1], L-coins[len(coins)-1]) )

print(changeMaking(coins, 4))