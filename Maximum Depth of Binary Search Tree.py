""" 1. Will the input having no element?
    2. Will there have same value in input?
    3. Will there exist negative element in input?
    4. What kind of data set will the input be? ex. arr? link list?
"""

# Traverse through all element to the leafs then return the maximum depth
input1 = [3, 9, 20, None, None, 15, 7]
input2 = []
input3 = [3, 9, 20, None, None, 15, 7, 12]
input4 = [1]
""" Input type is array 
    example: Input = [3,9,20,null,null,15,7]
             Depth    1 2  2    3    3  3 3
             2^x      0 1  1    2    2  2 2

    Thought: 
        1. Count element in array input (n)
        2. 2^i <= n <= 2^(i+1)
        3. i would be the depth of the last element
"""

i = len(input2)
dep = 0
while True:
    if i == 0:
        break
    if 2**dep > i:
        break
    else:
        dep += 1


print("Max Depth: %d" % dep)


"""
    1. What if input type is link list now?
    
    Thought:
        1. Recursively go through all nodes
        2. O(n): Log(n)
"""


def treeTravel(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    else:
        return max(treeTravel(root.left), treeTravel(root.right)) + 1