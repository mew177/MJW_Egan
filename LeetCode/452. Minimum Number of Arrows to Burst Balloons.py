# coding=utf-8
"""
            Question:
            1. This problem must have at least one shoot needed if there is no ø input?
            2.

            Idea:
            1. Main Idea is to find most overlapped point, that would be efficient to shoot more balloons in less shoot
            2. sort by x1
            3. x2 would be the limit point that it can be shoot
            4. if next balloon has this x2 in interval, it will be bursted in the same shoot
            5. if not, we must have one more shoot to burst that balloon

            Time Complexity:
            O(nlog(n)[sort] + n[traverse])

        """

points = [[10,16], [2,8], [1,6], [7,12]]

# sort them by x1
points = sorted(points)

# there might be negative x (different from time interval)
lp = float("-inf")
rp = float("-inf")
overlap = []

for point in points:
    # if shoot interval has no overlap with new interval
    if point[0] > rp and point[1] > rp:
        overlap.append([lp, rp])
        lp = point[0]
        rp = point[1]
    # if shoot interval has part of overlap with new interval
    elif point[0] <= rp and point[1] >= rp:
        lp = point[0]
        rp = rp
    # if shoot interval covere whole new interval
    elif point[0] < rp and point[1] < rp:
        lp = point[0]
        rp = point[1]
# add the last shoot interval
overlap.append([lp, rp])
# eliminate the base case
overlap.pop(0)
print(overlap)
print(len(overlap))