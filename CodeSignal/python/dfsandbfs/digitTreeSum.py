# Understanding
# DFS
# initialize cur
# if not t return []/None
# no restriction on space/time complexity 
# use recursion to travel depth of tree
# when left & right pointers are null go back to top
# initialize counter 

# Planning
#

# Execute

# Refactor/Reflect
def traverse(t, prev, enclist):
    if not(t.left or t.right):
        enclist.append(prev + str(t.value))
        return
    if t.left:
        traverse(t.left, prev + str(t.value), enclist)
    if t.right:
        traverse(t.right, prev + str(t.value), enclist)

def digitTreeSum(t):
    encodeList = []
    total = 0
    traverse(t, '', encodeList)
    for number in encodeList:
        total += int(number)
    return total