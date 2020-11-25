# Understanding
# block with dimensions 4 x n
# find # of ways you can fit blocks of 1 x 2
# rotate smaller blocks
# 4 possible rotations of smaller blocks

# example 4 x 1, 
    # output of fillingBlocks(n) = 1
# example 4 x 4,
    # output of fillingBlocks(n) = 36
# example 4 x 2,
    # output of fillingBlocks(n) = 5

# Planning
#

# Execute
# def fillingBlocks(n):

# Refactor/Reflection
def fillingBlocks(n):
    f = {
        1: 1,
        2: 5,
        3: 11,
        4: 36,
    }

    if n == 0:
        return 0
    if n < 5:
        return f[n]
    for i in range(5, n+1):
        f[i] = f[i-1] + 5*f[i-2] + f[i-3] - f[i-4]
    return f[n]