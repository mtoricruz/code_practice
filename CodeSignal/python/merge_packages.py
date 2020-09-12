#           i  
#           v  
# idx =  0  1  2   3   4
items = [4, 6, 10, 15, 16] 
# idx2 =       0   1   2
#                  ^
#                  j
limit = 21

def merge_packages(items, limit):
    # loop through items list
    for idx, i in enumerate(items):
        # diff = 21  - 4
        diff = limit - i
        #if 15 is in items[1+1:->]
        if diff in items[idx+1:]:
            # loop through items[1+1:->]
            for idx2, j in enumerate(items[idx+1:]):
                if j == diff:
                    return [idx + idx2 + 1, idx]
#   return empty array if no such pair equals limit
    return []

print(merge_packages(items, limit))

# R
# if j == diff:
#   if i > j:
#       return [idx + idx2 + 1, idx]