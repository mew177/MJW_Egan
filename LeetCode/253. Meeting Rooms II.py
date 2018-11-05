class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


"""
            Question:
            1. Will there happen to have negative time?
            2. 

            Idea:
            1. Sorted by start time
            2. assign to the room if new assignment start time is bigger than previous assignment end time
            3. If not, create a new room 

            Time Complexity:
            O(log(n) + n)
        """

intervals = [Interval(1, 6), Interval(2, 4), Interval(8, 9), Interval(4, 7), Interval(0, 1)]

intervals = sorted(intervals, key=lambda i: i.start)

rooms = []

for interval in intervals:
    assigned = False
    for i in range(len(rooms)):
        if interval.start >= rooms[i]:
            rooms[i] = interval.end
            assigned = True
            break
    if not assigned:
        rooms.append(interval.end)

print(len(rooms))
