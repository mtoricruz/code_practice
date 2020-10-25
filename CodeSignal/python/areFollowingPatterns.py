# Understanding
# strings and patterns are list of string types
# strings/patterns are same length of list
# final result needs return boolean t/f
# 2 hash tables 1 for strings 1 for patterns
# loop through each list and keep track of keys as [i] values
# initialize or increment counters for those keys
# check len of both dictionaries, if both equal return true else false

# Planning
# initialize strdict & patdict
# for elm in strings:
    # strdict[elm] = 1 if elm not in strdict else + 1
# for elm patterns:
    # patdict[elm] = 1 if elm not in patdict else + 1
# return if len(strdict) == len(patdict) else false

# Execution my attempt
def areFollowingPatterns(strings, patterns):
    strdict = patdict = {}
    for elm in strings:
        strdict[elm] = 1 if elm not in strdict else + 1
    for elm in patterns:
        patdict[elm] = 1 if elm not in patdict else + 1
    return len(strdict) == len(patdict)
# my passed 95% of test. Failed 100% because it doesnt account
# for patterns and strings lists with same number of keys but in different order

# Refactor/Reflection
# top answer
return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))
# this answer checks out because if one of zip lengths has extra key then it wouldn't be True

print(areFollowingPatters())