"""
            Question:
            1. Is this kind of dynamic programming?
            2.

            Idea:
            1.
        """

nums = [1, 2, 3, 4, 5]

rst = [1 for _ in range(len(nums))]

acc = 1
for i in range(len(nums)):
    rst[i] *= acc
    acc *= nums[i]

acc = 1
for i in range(len(nums) - 1, -1, -1):
    rst[i] *= acc
    acc *= nums[i]

print(rst)
