"""
    Main Idea: All function with TC O(1)
    Every input x: stored as [ smallest x after this position, x ]

"""

class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return self.stack[-2]

"""
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.order = []

    def push(self, x): # O(n)
        self.stack.append(x)
        index = 0
        for i in range(len(self.order)):
            if x > self.order[i]:
                index = i+1
                break
        self.order.insert(index, x)

    def pop(self): # constant time
        del self.order[self.order.index(self.stack[-1])]
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self): # constant time
        return self.order[0]
"""

stack = MinStack()
print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))
print(stack.getMin()) # -3
print(stack.pop())
print(stack.top()) # 0
print(stack.getMin()) # -2

