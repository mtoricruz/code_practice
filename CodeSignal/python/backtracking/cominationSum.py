# Understanding
# an array integers 'a' and a single int 'sum' 
# find all unique(create set) combos in a that add up to sum
# same number from 'a' can be used limitless times in a combo
# combinations themselves to be sorted in ascending - a<b<c<d - use sort() to sort combos in ascend
# elements in combo must be sorted in non-desc order - (1, 2, 2, 3)
# If no possible cominations that add up to sum, output to be string "Empty"
# Add combinations in format of "(2, 3, 4, 4)(1, 2, 2, 6)"

# Planning
#

# Execute

# Refactor/Reflection
def combinationSum(a, s):
    arr = sorted(set(a))
    ans = list(comb_recur([], arr, s))
    ans.sort()
    if len(ans) == 0:
        return 'Empty'
    else:
        return '({})'.format(')('.join(' '.join(map(str, row)) for row in ans))

def comb_recur(pref, arr, s):
    for idx, val in enumerate(arr):
        if val == s:
            yield pref + [val]
        elif val < s:
            yield from comb_recur(pref + [val], arr[idx:], s-val)
        elif val > s:
            break

# Learning 'yield' statement: The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.