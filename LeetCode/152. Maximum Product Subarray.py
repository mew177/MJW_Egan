"""
            Question:
            1. Seems like dynamic programming. Do we have enough space for memoization?
            2. There might be zero
            3. how large might the product be? over the size of int?
            4.

            Idea (innocent):
            1. two loop
            2. find max
            **O(n^2)**

            Idea (DP):
            1. Dynamic programming
            2. P[k] = the max product, and min product in subsequence X1~Xk
            3.
        """
nums = [1, 3, -1, 5, 3, -2, -4, 6, -3]

B = nums[::-1]
for i in range(1, len(nums)):
    nums[i] *= nums[i - 1] or 1
    B[i] *= B[i - 1] or 1
print(max(nums + B))

# ===================

p = [[1 for _ in range(len(nums))] for _ in range(len(nums))]

for i in range(len(nums)):
    for j in range(len(nums)):
        if j == i:
            p[i][j] = nums[j]
        elif j < i:
            p[i][j] = float("-inf")
        else:
            p[i][j] = p[i][j - 1] * nums[j]

M = float("-inf")
for row in p:
    M = max(M, max(row))
#print(M)
