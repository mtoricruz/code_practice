#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
# Understanding
# One BST traversal & o1 space complexity - no lists/dicts
# nodes left of key are < node's key
# nodes right of key are > node's key
# compareCounter of how many times i compare node value against kth value
# base cases:
    # 1. empty t return t
    # 2. t has 1 node then, k value set k = t
    # 3. t has 1 node and kth > # of t nodes
    # 4. # of t nodes > kth value
# kthSmallest = t
# keep track of how many nodes i visit?
# if compareCounter < k:
    # if currMax < max:
        #

# Planning
# curr = t.value
# compareCount = 0
# if curr < k:
    # compareCount += 1
    # kthSmallestInBST(curr.right, k)

# Execution - my attempt
def kthSmallestInBST(t, k):
    curr = t

    while curr:
        if not curr.left:
            k -= 1
            if k == 0:
                return curr.value
            curr = curr.right
        else:
            pred = find_pred(curr)
            if not pred.right:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                k -= 1
                if k == 0:
                    return curr.value
                curr = curr.right
    
    return None

def find_pred(t):
    pred = t.left

    while pred.right and pred.right != t:
        pred = pred.right
    return pred
    
# Refactor/Reflection