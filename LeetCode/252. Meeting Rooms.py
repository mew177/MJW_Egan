class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

"""
            Question:
            1. If there has no meeting to attend, then should return true?
            2. Will there has a negative interval?
            3. Is there possible to have two identical interval?
            4. Should they regared as the same, or two different meeting?

            Idea:
            1. Sort by start time
            2. P record end time of interval
            3. if P <= new interval start time, that means he is able to attend this meeting
            4. let P = end time of new interval
            5. if P > new interval start time, that means he is not able to attend this meeting
            6. return false
            ** O(log(n) + n)
        """
intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]

intervals = sorted(intervals, key=lambda i: i.start)
P = -1

for interval in intervals:
    if interval.start >= P:
        # he is able to attend this meeting
        P = interval.end
    else:
        # not able to attend this meeting
        print(False)
print(True)