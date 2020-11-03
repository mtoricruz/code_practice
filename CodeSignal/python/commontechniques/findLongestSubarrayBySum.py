# Understanding
# answer is 1 based (no 0th index)
# if no answer return [-1]
# if several answers, return the one with the smallest left bound
# initialize prefix sum
# no restriction on space/time complexity
# ask if we can sort array from start

# Planning
# loop through arr:
    # 

# Execute
def findLongestSubarrayBySum(s, arr):

# Refactor/Reflection
def findLongestSubarrayBySum(s, arr):
    total = j = 0
    res = (0, -1)
    for idx, val in enumerate(arr):
        total += val
        while j<=idx and total>s:
            total -= arr[j]
            j += 1
        if (total == s) and (res[1]-res[0]<idx-j):
            res=(j+1, idx+1)
    return res if res[0] else [-1]