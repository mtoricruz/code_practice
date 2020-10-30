# Understanding
# Morris' In Order Traversal
# curr & pred pointers
# helper function for finding pred
# as we traverse through nodes, decrementing kth int
# pred is pred relation to curr node
# BST left nodes are < node's key
# right nodes are > node's key
# left/right subtrees are also BST

# Planning
# initialize curr pointer
# while curr exists:
    # if not curr.left:
        # k -= 1
        # if k == 0:
            # return curr.value
        # curr = curr.right
    # else:
        # pred = find_pred(curr)
        # if not pred.right:
            # pred.right = curr
            # curr = curr.left
        # else:
            # pred.right = None
            # k -= 1
            # if k == 0:
                # return curr.value
            # curr = curr.right
# return None            

# create find_pred helper function(t):
    # pred initialized to equal t.left
    # while pred.right and pred.right != t:
        # pred = pred.right
    # return pred

# Execution

# Refactor/Reflection