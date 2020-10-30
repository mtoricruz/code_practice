# Understanding
# no restriction on space complexity
# keep track of currt1 and currt2 pointers
# DFT of BST
# traverse all nodes on both trees once starting point initialized on both sides
# traverse until discrepancy identified
# append value that doesn't have match to a list
# DFT and once we reach end return True
    # while len(list) > 0:
        # return False
    # traverse

# Planning
# if ct1.value != ct2.value:
    # if ct1 < ct2:
        # ct1 = ct1.left
    # else:
        # ct1 = ct1.right
# else:
    # if ct1.right and ct2.right:
        # ct1prev, ct2prev = ct1, ct2
        # ct1 = ct1.right
        # ct2 = ct2.right
#

# Execution - my attempt

# Refactor/Reflection
def isSubtree(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return True
    
    if isEqual(t1, t2):
        return True
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)

def isEqual(t1, t2):
    if t1 is None:
        return t2 is None
    if t2 is None:
        return False
    
    if t1.value != t2.value:
        return False
    
    return isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)
