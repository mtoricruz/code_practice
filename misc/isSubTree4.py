def isSubTree(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return True
    
    if isEqual(t1, t2):
        return True
    
    return isSubTree(t1.left, t2) or isSubTree(t1.right, t2)

def isEqual(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return False
    
    if t1.value != t2.value:
        return False

    return isEqual(t1.right, t2.right) and isEqual(t1.left, t2.left)