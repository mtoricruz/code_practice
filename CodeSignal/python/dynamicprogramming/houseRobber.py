# Understanding
# if 2 adjacent indicies are robbed in same night, alarm triggers
# index value is amount of money in houses, indicies are houses
# does sorting list influence algorithm?
# 
#v     v     v     v
[1, 2, 3, 4, 5, 6, 7]
# output should be 2

# Planning
# no clue, study python tutor viz to understand solution

# Execution - my attempt

# Refactor/Reflection
def houseRobber(nums):
    a = b = 0
    for i in nums:
        a, b = max(b+i, a), a
    return max(a, b)