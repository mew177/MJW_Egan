"""
            Question:
            1. Are entries all numbers? or can they be characters?
            2. How large this tree can be?
            3. What kind of data structure is the input? linked list?



            Idea:
            1. Basic BST usage
            2. If root.val == val, return root
            3. If root.val > val, val should exist at left subtree
            4. If root.val < val, val should exist at right subtree
            5. find until root is null, then return None.
"""

root = [4,2,7,1,3]
val = 2

def find(root, val):
    if root == None:
        return None
    else:
        if root.val == val:
            return root
        elif root.val > val:
            return find(root.left, val)
        else:
            return find(root.right, val)


print(find(root, val))