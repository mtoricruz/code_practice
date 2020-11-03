# Understanding
# loop through range(len(nums)):
# initialize summary array
# nums already sorted

# Planning
# initialize start = nums[0]
    # while i != nums[-1]
        # if nums[i+1] > (nums[i] + 1):
            # initialize end = i
            # summary.append("%s->%s" % (start,end))
            # start = i
            # end = 0
    # summary.append("%s" % (nums[i]))
# return summary

# Execute
# def composeRanges(nums):
#     summary = []
#     for i in nums:
#         if not start:
#             start = i
#         while i != nums[-1]:
#             if nums[i+1] > (i+1):
#                 end = i
#                 summary.append("%s->%s" % (start, end))
#                 start = nums[i]
#                 end = 0
#         summary.append("%s" % (nums[-1]))
#     return summary

# Refactor/Reflection
def composeRanges(nums):
    summary = []
    while nums:
        start = end = nums.pop(0)
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        summary.append(str(start) + ('', '->' + str(end))[start != end])
    return summary