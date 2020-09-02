#            0  1   2   3
#               i
nums_list = [2, 7, 11, 15]
targ = 9
# { 7 : 0 }

def twoSum(nums, target):
    d = {}

    for i in range(len(nums)):
        res = target - nums[i]
        if nums[i] in d:
                      # 0 , 1
            return [d[nums[i]], i]
        else:
            d[res] = i

def bruteForcetwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                return [i, j]

print(twoSum(nums_list, targ))