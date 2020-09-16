# Understanding
# given a SLL of integers
# check if palindrome
# return true if, false if not
# initialize nums_list
# traverse through SLL
# appending each node into nums_list
# when end is reached, come out of while loop
# result = nums_list.reverse() == nums_list:
# return result


# Planning
# initialize nums_list
# while l != None:
    # nums_list.append(l.value)
    # l = l.next
# result = nums_list == nums_list.reverse()
# return result

# Execute
def isListPalindrome(l):
    nums_list = []
    while l != None:
        nums_list.append(l.value)
        l = l.next
    result = nums_list == nums_list[::-1]
    return result



# R
# I believe .reverse() was returning none because it actually updates the list it's reversing
# instead of copying it, so i was trying to compare a list, change it mid logic, and compare it against
# the same list.
# [::-1] is another way (slicing) to reverse a list in python