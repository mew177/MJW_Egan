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

stack = MinStack()
print(stack.push(-2))
print(stack.push(0))
print(stack.push(-3))
print(stack.getMin()) # -3
print(stack.pop()) # -3
print(stack.top()) # 0
print(stack.getMin()) # -2

