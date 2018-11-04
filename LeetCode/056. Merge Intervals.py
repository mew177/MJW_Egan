class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
            Question:
            1. Is it possible to have two same interval?
            2. Will there have negative numbers?
            3. Is there 0 interval?
            4. Are they all sorted?

            Idea:
            1. Two pointer
            2. [x1, y1] let Lp = x1, Rp = y1
            3. [x2, y2] if x2 <= Lp, Lp remain
            4. [x2, y2] if y2 <= Rp, Rp remain
            5. when x3 > Rp, Lp = x3, Rp = y3

            Time Complexity:
            O(log(n) + n)
"""

intervals = [Interval(1, 4), Interval(0, 3), Interval(5, 8), Interval(8, 13), Interval(6, 7)]

# sort interval incremently with start time
# remove the possiblility that new interval has smaller start time than previous
intervals = sorted(intervals, key=lambda interval: interval.start)
# initialization Lp, Rp = 1, there will not be negative interval
Lp = -1
Rp = -1
merged = []

for interval in intervals:
    # when new interval has no overlap with Lp~Rp interval
    if interval.start > Rp and interval.end > Rp:
        merged.append(Interval(Lp, Rp))
        Lp = interval.start
        Rp = interval.end
        # when new interval overlapped with Lp~Rp, including start == Rp
    elif interval.start <= Rp and interval.end > Rp:
        Lp = Lp
        Rp = interval.end
        # when new interval is in Lp~Rp interval
    elif interval.start < Rp and interval.end < Rp:
        Lp = Lp
        Rp = Rp

# append the last interval Lp~Rp
merged.append(Interval(Lp, Rp))
# get rid off the first (Lp, Rp) which is (-1, -1)
merged.pop(0)
for i in intervals:
    print(i.start, i.end)
print("----")
for i in merged:
    print(i.start, i.end)