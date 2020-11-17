a = ["aba",'asdfj;laoepijaklvcnxkl;zkadjsf', "aa", "ad",'asdfj;laoepijaklvcnxkl;zkadjsf', "vcd", 'asdfj;laoepijaklvcnxkl;zkadjsf', "aba", 'l0l0l0l0l0l0l0l']

# def allLongestStrings(inputArray):
#     maxStrLen = 0
#     results = []
#     for string in inputArray:
#         if len(string) > maxStrLen:
#             maxStrLen = len(string)
#     for string in inputArray:
#         if len(string) == maxStrLen:
#             results.append(string)
#     return results


# idea, sort input arr by len of strings
# store last element in sorted arr in variable
# loop through inputarray and check if each str is < maxstrlen
# if so, remove from input arr
# after it reaches end of loop, return input array
# O(1) space complexity achieved
# Refactor/Reflection
def allLongestStrings(inputArray):
    # sorts inputArray by length of string
    sortedArr = sorted(inputArray, key=len)
    # takes the longest string(at end of array) and stores length
    maxStrLen = len(sortedArr[-1])
    # loop through each string in enumerate(sortedArr) - to keep track of index
    for idx,string in enumerate(sortedArr):
        # when the first string in sorted arr matches maxstrlen
        if len(string) == maxStrLen:
            # delete the rest of strings from sorted array to the left of the first maxlenstr 
            del sortedArr[:idx]
    # return sortedArr
    return sortedArr

print(allLongestStrings(a))