# Understanding
# queries is a list of integers
# integers represent tree node value to remove from BST
# if query[i] not in t: continue
# if remove query[i] then change pointers to point to left/right most subtree
# if t == None:
    # return None


# Planning
# curr = t
# for query in queries:
    # if query == curr.right || query == curr.left:
        # 


# Execute
# def deleteFromBST(t, queries):

# Refactor/Reflection
def deleteFromBST(t, queries):
    for q in queries:
        t = deleteNode(t, q)
    return t

def deleteMax(t):
    if not t.right:
        return t.left
    t.right = deleteMax(t.right)
    return t

def processLeft(t, x):
    rm = t.left
    while rm.right:
        rm = rm.right
    rm.left = deleteMax(t.left)
    rm.right = t.right
    return rm

def deleteNode(t, x):
    if not t:
        return t
    if t.value == x:
        if not t.left:
            return t.right
        return processLeft(t, x)
    else:
        if x < t.value:
            t.left = deleteNode(t.left, x)
        else:
            t.right = deleteNode(t.right, x)
    return t