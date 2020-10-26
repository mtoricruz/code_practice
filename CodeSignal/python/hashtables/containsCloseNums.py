# Understanding
# receiving a list and an int
# where nums[i] = nums[j], the difference(space) between
# those values is less than or equal to k
# loop thru nums
# initialize an  empty dictionary
# intialize counter 1
# else + 1, store dupe in variable j
# for item in nums:
# if j equals item:
# store item in variable i
# return len(nums[idx:jdx]) <= k

# Planning
# d = {}
# for number, index in enumerate(nums):
#   if number not in d:
#       d[number] = 1  
#   else:
#       j = number
#       jdx = index
#       break
# for number, index in enumerate(nums):
#   if j == number:
#       i = number
#       idx = index
# print(len(nums[idx:jdx]))
# return len(nums[idx:jdx]) <= k

# Execution my attempt
def containsCloseNums(nums, k):
    d = {}
    j, i = 0, 0
    idx, jdx = 0, 0
    while nums:
        for idx, num in enumerate(nums):
            if num not in d:
                d[num] = 1
            else:
                j = num
                jdx = idx
                break
        for index, num in enumerate(nums):
            if j == num:
                i = num
                idx = index
        return len(nums[idx:jdx]) <= k

# Refactor/Reflection
def containsCloseNums(nums, k):
    d = {}
    for idx, num in enumerate(nums):
        if num in d:
            if idx - d[num] <= k:
                return True 
            else:
                d[num] = idx
        else:
            d[num] = idx
    return False