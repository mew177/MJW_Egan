""" Question:
        1. Will n be zero?
        2. Will integers be negative?
        3. Will there be the same value?
        4. How large will the largest value be?
        5. ...

    Thought1:
        1. smallest number must paired with the second smallest number
        2. Sort them from small to large then paired them orderedly


    How much is Complexity:

"""

nums = [1,4,3,2]
Output = 4

nums = sorted(nums)
Sum = 0
for i in range(0, len(nums), 2):
    Sum = Sum + nums[i]

print Sum