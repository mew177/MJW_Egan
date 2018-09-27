"""
    Question:
    1. Will there be negative number? a element that is not a number?
    2. Will there be continueous same number? Is that possible for them to be the mountain peak?
    3. Will the peak appear at first or last position? that will not fit the rule A[0] < A[1] <...< A[i] > A[i+1]...

    Idea:
    1. Find peak in a 2D array => binary search
    2. Advantage of binary search => Time Complexity: (log n)
"""

A = [0, 1, 0]

# upper bound: up
# lower bound: lp
up = len(A)
lp = 0
while True:
    if A[(up + lp) / 2] < A[((up + lp) / 2) + 1] and A[((up + lp) / 2) - 1] < A[((up + lp) / 2)]:
        lp = (up + lp) / 2
    elif A[(up + lp) / 2] > A[((up + lp) / 2) + 1] and A[((up + lp) / 2) - 1] > A[((up + lp) / 2)]:
        up = (up + lp) / 2
    else:
        # print the index of mountain peak
        print((up+lp)/2)
        break