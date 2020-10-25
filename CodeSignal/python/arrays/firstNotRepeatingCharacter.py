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
# for v in d:
#   if v == 1:
#       return k
#   else:
#       continue
# return '_'


string = 'abacabad'

# v
# a b a c a b a d

def firstNotRepeatingCharacter(s):
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

#   for idx in the range of s length
#   range makes integer iterable
    for i in range(len(s)):
      # if the value of a key in d is 1
        if d[s[i]] == 1:
        #   return idx value of string
            return s[i]
  # return '_' if no unique characters        
    return '_'

print(firstNotRepeatingCharacter(string))
