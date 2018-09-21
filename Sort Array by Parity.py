""" Question:
        1. Will there be zero?
        2. Will there have the same value more than one?
        3. Can I have more memory used? Or just change in that memory given?
        4. O(n) might smaller than?

    Same as moving 0 to the front of array
        1. Given two pointer initialized from first and last element
        2. Left.P + 1 until find the first even number
        3. Right.P -1 until find the first odd number
        4. Exchange their value
        5. Repeat until Left.P meet Right.P

    Additional Question:
        1. What if I need to sort them from smallest to largest in even set and odd set?
"""

A = [2, 4, 5, 1, 7, 8, 3, 9]
"""
Special input:
    [0]
    [0, 2]
"""

lp = 0  # 0
rp = len(A) - 1  # n-1

if len(A) == 1:
    print("Result:", A)

while True:
    while A[lp] % 2 == 0 and lp < len(A) - 1:
        lp += 1
    while A[rp] % 2 == 1 and rp > 0:
        rp -= 1
    if lp < rp:
        A[lp], A[rp] = A[rp], A[lp]
    else:
        break

print("Result:", A)
