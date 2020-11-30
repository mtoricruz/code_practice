# Understanding
# reverse strings within parentheses
# loop through input string to keep track of opening/closing parentheses
# possibly initialize counter of opening parentheses
# .includes('(', ')')

# Planning
# toBeReversed = []
# stringCounter = 0
# for char in inputString:
    # if inputString[char-1] == '(':
        # stringCounter += 1
    # if char == ')':
        # stringCounter -= 1
        # reversedWord = inputString.join(toBeReversed)
    # if stringCounter > 1:
        # toBeReversed.append(char)
# result = reversedWord[::-1]
# return result

# Execute 
# def reverseInParentheses(inputString):
#     toBeReversed, stringCounter = [], 0
#     for char in inputString:
#         if char == '(':
#             stringCounter += 1
#         if char == ')':
#             stringCounter -= 1
#             reversedWord = inputString.join(toBeReversed)
#             print(reversedWord)
#         if stringCounter > 1:
#             toBeReversed.append(char)
#     return inputString

# Reflect/Refactor
def reverseInParentheses(inputString):
    for char in range(len(inputString)):
        if inputString[char] == '(':
            start = char
        if inputString[char] == ')':
            end = char
            return reverseInParentheses(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
    return inputString