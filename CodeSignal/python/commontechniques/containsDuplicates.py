# Understanding 
# store elements in dictionary
# key = element / value = # of times appeared
# return T/F whether or not arr contains dupes
# there's no restriction on space complexity

# Planning
# initialize an empty dictionary
# for i in a:
    # if i not in d:
        # d[i] = 1
    # else:
        # d[i] += 1

# for value in d.values():
    # return True if value > 1 else False


# Execution - my attempt
# def containsDuplicates(a):
#     d = {}
#     for i in a:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     for value in d.values():
#         return True if value > 1 else False

# Refactor/Reflection
# 2nd attempt after google searches
def containsDuplicates(a):
    d = {}
    dupes = []
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            dupes.append(i)
    while a:
        return len(dupes) > 0
    return False

# top answer
def containsDuplicates(a)
    return len(set(a)) != len(a)