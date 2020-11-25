# Understanding
# no restriction on space/time complexity
# loop a subtract elm from v 
# then loop thru b and if diff == elmb 
# return True
# return False

# Planning
# for elm in a:
    # diff = v - elm
    # for elmb in b:
        # if elmb == diff:
            # return True
        # else:
            # return False
# return False

# Execution - my attempt
# def sumOfTwo(a, b, v):
#     results = []
#     for elm in a:
#         diff = v - elm
#         for elmb in b:
#             if elmb == diff:
#                 results.append(elmb)
#     return len(results) > 0
        
# Refactor/Reflection
def sumOfTwo(a, b, v):
    if not a or not b:
        return False
    b = set(b)

    for elm in a:
        if (v-elm) in b:
            return True
    return False