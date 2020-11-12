# Understanding
# we can loop through array
# store difference of arr[i] - num
# check to see if diff is in arr
# if so, add subset to results arr
# does .sort() solve the lexicographical order?
# 

# Planning
# initalize results arr
# if arr is None:
    # return []
# if num in arr:
    # return [num]
# loop through array
    # diff = num-i
    # if diff in arr:
    # results += [i, diff]
# 

# Execute
# def sumSubsets(arr, num):
#     results = set()
#     if not arr:
#         return [results]
#     for i in arr:
#         diff = num-i
#         if diff in arr:
#             results += [[i, diff]]
            
#     print(results)

# Refactor/Reflect
def sumSubsets(arr, num):
    results = set()
    
    def find_sum(t, a, n):
        if n == 0:
            results.add(t)
        for i in range(len(a)):
            if a[i] <= n:
                find_sum(t+(a[i],), a[i+1:], n-a[i])
            else:
                return
    find_sum((), arr, num)
    return sorted(list(results))