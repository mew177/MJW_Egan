input1 = [1, 3, 5, 7, 10, 12] # even number of element
input2 = [1, 3, 4, 7, 10] # odd number of element
input3 = [5] # one element

def bs (numbers, leftBound, rightBound, target):
    if len(numbers) <= 1:
        if numbers[0] == target:
            return 0
        else:
            return None

    if leftBound == rightBound-1:
        if numbers[rightBound] == target:
            return rightBound
        elif numbers[leftBound] == target:
            return leftBound
        else:
            return None
    mid = (leftBound + rightBound)/2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        # target is at the right side to mid
        return bs(numbers, leftBound, mid, target)
    else:
        # target is at the right side to mid
        return bs(numbers, mid, rightBound, target)



target = 8
#print("%d, is at index %d in list" % (target, bs(input1, 0, len(input1)-1, target)))
print(bs(input3, 0, len(input3)-1, target))
print(input3)