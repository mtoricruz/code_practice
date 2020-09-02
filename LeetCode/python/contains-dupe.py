# Given an array of integers, find if the array contains any duplicates.
arr_of_ints = [1, 2, 2, 3, 3, 4, 5]
arr_of_ints2 = [1, 2, 3, 4, 5]
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

# U
# array of integers 
# identify if duplicate integers are in passed array
# if yes, return true else return false

# P
# create empty dict to count how many times an int appears = {}
# for item in dict:
    # if item not in dict:
        # set key to value 1 and to begin counting
    # else:
        # dict[value] += 1
# if dict[value] < 2:
    # return True
# else:
    # return False

    

# E
def containsDuplicate(nums):
    d = {}
    for item in nums:
        if item not in d:
            d[item] = 1
        else:
            return True
    return False
    # if d[item] >= 2:
    #     return True
    # else:
    #     return False
    # for item in d:
    #     if d[item] >= 2:
    #         return True
    # return False

print(containsDuplicate(arr_of_ints2))
# containsDuplicate(arr_of_ints)

# R
# convert final if else statement to a ternary statement
# Double check instructions because i was returning true if there wasn't a duplicate. I had the results reversed.
# Thankfully a simple/quick preventable fix