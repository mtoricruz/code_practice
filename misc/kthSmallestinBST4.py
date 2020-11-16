# Planning
# curr = t
# while curr:
    # if not t.left:
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

# find_pred(t):
# pred = t.left
# while pred.right and pred.right != t:
    # pred = pred.right
# return pred
def kthSmallestinBST4(t, k):
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