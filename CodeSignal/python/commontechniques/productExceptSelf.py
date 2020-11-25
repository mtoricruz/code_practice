# Understanding
# calculate all values of f % m
# take those values and add together = g
# return g % m

# Planning
#

# Execute
# def productExceptSelf(nums, m):

# Refactor/Reflection:
def productExceptSelf(nums, m):
    s, p = 0, 1
    for num in nums:
        s, p = (p + s*num) % m, p*num % m
    return s