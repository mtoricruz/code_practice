# Understanding
# implement recursive solution
# base case is right/left node is null to signal leaf node
# while t.left and t.right != None implement recursion
# return False otherwise. 
# root-to-leaf path 

# Planning
#

# Execution - my attempt
def hasPathWithGivenSum(t, s):
    current_sum = 0
    while t.left or t.right:
        if t.right or t.left == s - current_sum:
            return True
        else:
            hasPathWithGivenSum(t, s)
    return False

# Refactor/Reflection
def hasPathWithGivenSum(t, s):
    # base case
    if t is None:
        return False
    s -= t.value  
    left = t.left
    right = t.right   
    # at leaf node, from root
    if left is None and right is None and s == 0:
        return True
    return hasPathWithGivenSum(left, s) or hasPathWithGivenSum(right, s)
    