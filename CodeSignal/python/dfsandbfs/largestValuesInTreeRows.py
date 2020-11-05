# Understanding
# BFS to find largest node
# initialize q = [t]
# return array of largest val in each row
    # initialize a results arr + levelNodes arr
    # depth counter
# each level we can append node.value to levelNodes arr
# results.append(max(levelNodes))
# while q:
    # if t.left == None and t.right == None:
        # return results

# Planning
# results, levelNodes = [], []
# q = [t]
# depth = 0
# if not t:
    # return []

# while q:
    # if t.right:
        # levelNodes.append(t.right)
    # if t.left:
        # levelNodes.append(t.left)
    # depth += 1
# while depth > 0:
    # results.append(max(levelNodes))
    # levelNodes = []
# return results


# Execute

# Refactor/Reflection
def largestValuesInTreeRows(t):
    if not t:
        return []
    results, levelNodes = [], [t]
    while levelNodes:
        temp = []
        maxVal = levelNodes[0].value
        for node in levelNodes:
            if node.value > maxVal:
                maxVal = node.value
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        levelNodes = temp
        results.append(maxVal)
    return results

# learned there is no need for depth counter