# Understanding
# return a list of possible sequences
# base cases of 0 & 1:
    # return [[]] if n == 0
    # if n == 1 and k == 1: return [[1]]
# results list can be initialized
# algo to build sequences
# append those sequences to results
# results must be sorted -> what happens when we just .sort()
# Current idea:
    # based on n and k integers determine how many possible unique sequences and store in variable d
    # with d number of sequences, create lists with numbers between 1 - k until d number of unique sequences
    # exist, then append into results and sort

# Planning
# results = []
# while n:
#   

# Execute
# def climbingStaircase(n, k):
#     if n == 0: return [[]] 
#     if n == 1 and k == 1: return [[1]]

# Refactor/Reflection
def climbingStaircase(n, k):
    return climb(n, k, [])

def climb(n, k, jumps):
    if n==0:
        return [jumps]
    out = []
    for i in range(1, k+1):
        if i > n:
            continue
        temp = jumps + [i]
        out += climb(n-i, k, temp)
    return out