# Understanding
# Create iterative solution(no recursion)
# no restriction space complexity
# use list to store nodes throughout traversal
# curr/ rightPoint/ leftPoint
# BFS since we will move through each level

# Planning
# Initialize Pointers
# initialize empty list
# while curr:
    # if t.left:
        # leftPoint = t.left
        # list.append(leftPoint)
    # if t.right:
        # rightPoint = t.right
        # list.append(rightPoint)
     
# Execution
# def traverseTree(t):
#     if not t:
#         return []
#     curr = t
#     leftPoint = rightPoint = 0
#     results = []
#     while curr:
#         if t.left:
#             leftPoint = t.left
#             results.append(leftPoint)
#         if t.right:
#             rightPoint = t.right
#             results.append(rightPoint)
        

# Refactor/Reflection
def traverseTree(t):
    if not t:
        return []
    results = []
    queue = [t]

    while queue:
        v = queue.pop(0)
        results += [v.value]
        if v.left:
            queue += [v.left]
        if v.right:
            queue += [v.right]
    return results