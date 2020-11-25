# Understanding
# a-z is encoded with numbers 1-26
# in order; a-1, b-2, z-26
# maximum num value that can be decoded is 26
# find total # of ways the message can be decoded
# return the answer % 10**9 + 7
# base cases:
    # 1. if message is empty, return 1
    # 2. if message len is 1
# no restriction on space/time complexity 
# develop a first pass solution 
# store results in a separate data structure

# Planning

# Execute
def mapDecoding(message):
    results = 0
    if not message:
        return 1
    for letter in message:
        if letter < 26:
            results += 1

# Refactor/Reflect
def mapDecoding(message):
    a, b = 1, 0
    m = 10**9 + 7
    for i in range(len(message)-1, -1, -1):
        if message[i] == '0':
            a, b = 0, a
        else:
            a, b = (a + (i+2 <= len(message) and message[i:i+2] <= '26') * b) % a, a
    return a