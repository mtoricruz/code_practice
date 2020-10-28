# Understanding
# base cases:
    # 1 if t is None = return False
    # 2 if t is 1 node = return True
# create 2 pointers 
    # 1 for left & 1 for right side
# compare values of left children and right children on other side
#        1
#      /   \
#     2lp   2rp
#    / \   / \
#   3lp2 4 4   3rp2

# Planning
# check base cases 1 & 2
# initialize L/R pointers = t
# while t.left != None and t.right != None:
    # return isTreeSymmetric(t.left) or isTreeSymmetric(t.right)

# Execution - my attmpt
def isTreeSymmetric(t):
    if t is None:
        return True
    if t.right is None and t.left is None:
        return True
    leftPointer, rightPointer = t.left, t.right
    while leftPointer is not None and rightPointer is not None:
        if leftPointer == rightPointer and rightPointer == leftPointer:
            return isTreeSymmetric(leftPointer) or isTreeSymmetric(rightPointer)
        else:
            False

# Refactor/Reflection
def isTreeSymmetric(t):
    def helper(leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None and rightNode is not None:
            return False
        if leftNode.value == rightNode.value:
            return helper(leftNode.left, rightNode.right) and helper(rightNode.left, leftNode.right)
        else:
            False
            
    if t is None:
        return True

    return helper(t.left, t.right) 