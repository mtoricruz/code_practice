# Understanding
# loop through array and switch heights in non-desc order
# can't move trees (-1's)
# switch heights possibly multiple indexes away if greater than currMaxHeight

# Planning
# initialize maxHeightIndex = currHeightIndex = 0 
# loop thru a
    # currHeightIndex = idx
    # if a[idx] != -1:
        # if a[currHeightIndex] > a[maxHeightIndex]:
            # maxHeightIndex = currHeightIndex
        # if a[currHeightIndex] < a[maxHeightIndex]:
            # a[maxHeightIndex] = a[currHeightIndex]
            # maxHeightIndex = currHeightIndex

# Execute    
# def sortByHeight(a):
#     maxHeightIndex = currHeightIndex = 0
#     for idx, hgt in enumerate(a):
#         currHeightIndex = idx
#         if a[idx] != -1:
#             if a[currHeightIndex] > a[maxHeightIndex]:
#                 maxHeightIndex = currHeightIndex
#             if a[currHeightIndex] < a[maxHeightIndex]:
#                 a[maxHeightIndex] = a[currHeightIndex]
#                 maxHeightIndex = currHeightIndex
#     return a

# Reflect/Refactor
def sortByHeight(a):
    for num in range(len(a)):
        if a[num] == -1:
            continue
        for hght in range(len(a)):
            if a[num] < a[hght]:
                a[num], a[hght] = a[hght], a[num]
    return a