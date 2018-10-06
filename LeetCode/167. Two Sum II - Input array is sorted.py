"""
            Question:
            1. Will there be duplicate number? Does it matter?
            2. Will there be negative number? Does it matter?
            3. Will the target be a negative number?

            Idea(Time Limit Exceeded):
            1. Go from 1 to n,
            2. Create a array to store the complement number
            e.g. A[1] = 1, target = 9; then Com[1] = 9-1 = 8
            3. Find if there's a complement number equal to A[x]

            Time Complexity:
            O(n + m)  n = numberListSize, m = ComplementListSize

            Idea:
            1. Set two pointer start tranverse from left most and right most
            2. if A[lp] + A[rp] == k return [lp, rp]
            3. if A[lp] + A[rp] > k, rp -= 1
            4. if A[lp] + A[rp] < k, lp += 1

            Time Complexity:
            O(n) n = numberListSize

        """

numbers = [2,7,11,15]
target = 9

lp = 0
rp = len(numbers) - 1

while lp < rp:
    if numbers[lp] + numbers[rp] - target > 0:
        rp -= 1
    elif numbers[lp] + numbers[rp] - target < 0:
        lp += 1
    else:
        print([lp + 1, rp + 1])