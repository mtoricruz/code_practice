# Understanding
# o(1) space complexity (no datastructures to add nodes)
# Morris in order traversal to solve problem
    # curr / pred pointers
    # helper function to find pred
# left subtree < key node
# right subtree > key node
# start at root
# decrement k

# Planning
# initialize curr pointer

# while curr exists:
    # if not curr.left:
        # decrement k
        # check if k == 0:
            # return curr.value
        # curr = curr.right
    # else:
        # pred = find_pred(curr)
        # if not pred.right:
            # pred.right = curr
            # curr = curr.left
        # else:
            # pred.right = None
            # decrement k
            # if k == 0:
                # return curr.value
            # curr = curr.right
# def find_pred(t):
    # pred = t.left
    # while pred.right and pred.right != t:
        # pred = pred.right
    # return pred

# Execution
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

def find_pred(t):
    pred = t.left
    while pred.right and pred.right != t:
        pred = pred.right
    return pred

# Refactor/Reflection
