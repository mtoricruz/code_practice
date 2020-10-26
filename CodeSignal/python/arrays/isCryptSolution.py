# Understanding
# isCrypt takes 2 args, 
# 1. 'crypt' an array of 3 non-empty strings
# 2. 'solution' an array containing mapping of letters and digits
# using solution, decode the 3 strings and identify num values of each letter
# if crypt as integers is a valid sum equation with NO leading 0's return True
# if it is not valid and/or has leading 0's return False

# Plan
# split string words into letters
# convert solution list into dictionary
# where letter(k): number(v)
# loop through letters and match against dictionary

c_msg = ["SEND", "MORE", "MONEY"]
sol =  [['O', '0'],
        ['M', '1'],
        ['Y', '2'],
        ['E', '5'],
        ['N', '6'],
        ['D', '7'],
        ['R', '8'],
        ['S', '9']]

def isCryptSolution(crypt, solution):
    # creating dictionary for solution arg
    d = dict(solution)
    # create convert helper function 
    def convert(c):
        # returns the value 'number'
        return d[c]
    # create new list to store integers for equation
    decoded = list()

    for word in crypt:
        # num variable decrypts words into string of nums based off dict
        # after decrypt of each word is complete, join string numbers into 1 string value
        num = ''.join([convert(c) for c in word])
        # check if first number in num is a leading 0 and the string is more than 1 number
        if num[0] == '0' and len(num) > 1:
            return False
        # skip if falsse and append the number to decoded
        decoded.append(int(num))
    # returns True if equation is correct, else returns False
    return decoded[0] + decoded[1] == decoded[2]

print(isCryptSolution(c_msg, sol))