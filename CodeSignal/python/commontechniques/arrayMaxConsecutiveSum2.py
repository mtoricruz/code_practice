# Understanding
# loop through list
# currMax and update as new possible contiguous sum is found
# 

# Planning
# currMax = 0
# for i in inputArray:
    # tempSum = i + i[i+1]
    # if currMax > tempSum:
        # continue
    # else:
        # currMax = tempSum
# return tempSum

# Execution

# Refactor/Reflection
def arrayMaxConsecutiveSum2(inputArray):
    currSum = 0
    maxSum = inputArray[0]
    for i in inputArray:
        tempSum = i + currSum
        if tempSum > 0:
            currSum = tempSum
        else:
            currSum = 0
        if tempSum > maxSum:
            maxSum = tempSum
    return maxSum