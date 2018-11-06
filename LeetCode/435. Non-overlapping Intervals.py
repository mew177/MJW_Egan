class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


"""
            Question:
            1. Is there negative boundary?
            2. Be aware of ø input
            3.

            Idea:
            1. Greedy algorithm, Earliest deadline first
            2. sorted by end time
            ***O(nlog(n))***
        """


intervals = [ [1,2], [2,3], [3,4], [1,3] ]

intervals = sorted(intervals, key=lambda i: i.end)

p = float("-inf")
removed = 0

for interval in intervals:
    if interval.start >= p:
        p = interval.end
    else:
        removed += 1
print(removed)