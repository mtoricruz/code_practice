# Understanding
# identify sum of individual queries
# sum of all queries and return that number
# no restriction on space complexity - store indivudal sums
# in list and then use sum() on list

# Planning
# initialize endSum list
# loop through queries
    # start = q[i][0]
    # end = q[i][1]
    # list_of_integers = nums[start:end]
    # endSum.append(sum(list_of_integers))
# results = sum(endSum)
# return results

# Execution
# def sumInRange(nums, queries):
#     endSum = []
#     for i in queries:
#         start = i[0]
#         end = i[1]
#         list_of_integers = nums[start:end+1]
#         endSum.append(sum(list_of_integers))
#     results = (sum(endSum) % (10**9 + 7))
#     return results

# Refactor/Reflection
def sumInRange(nums, queries):
    range_sum = [nums[0]]
    total = 0
    for i in nums[1:]:
        range_sum.append(range_sum[-1]+i)
    for j in queries:
        if j[0] == 0:
            total += range_sum[j[1]]
        else:
            total += range_sum[j[1]] - range_sum[j[0]-1]
    return total % (10**9 + 7)