# Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.

# EXAMPLE
# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.

# Understand
# given a STRING of lowercase letters
# Find/return the FIRST instance of a non-repeating character
# If no uniques, return '_'

# Plan
# d = {}
# for letter in s:
#   if letter not in d:
#       d[letter] = 1
#   else:
#       d[letter] += 1
# for k, v in d:
#   if v == 1:
#       return k
#   else:
#       continue
# return '_'


string = 'abacabad'

def firstNotRepeatingCharacter(s):
    d = {}
    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    for k, v in d.items():
        if v == 1:
            return k
        else:
            continue
    return '_'

print(firstNotRepeatingCharacter(string))
