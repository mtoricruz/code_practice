# Understanding
# base cases:
    # 1. n = 1 return 1
    # 2. n = 2 return 2
    # 3. climbingStairs(n-1) + climbingStairs(n-2)

# Planning

# Execution - my attempt
# def climbingStairs(n):
#     if n == 1 or n == 2:
#         return n
#     return climbingStairs(n-1) + climbingStairs(n-2)

# Refactor/Reflection
def climbingStairs(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + b, a
    return a


    