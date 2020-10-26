# Understanding
# string = []
# swapping indicies of strings based on pairs ex: [[1, 4], [3, 4]]
# loop thru pairs, pairs[0][4] = pairs[0][1] 
# while pairs:
# otherwise return string

# Planning
# initialize string variable to be empty array & result variable as empty string
# while pairs:
    # split each letter in str
    # for each letter in str:
        # string.append(letter)
    # for each pair in pairs:
        # swap of characters
        # string[pair[1]] = string[pair[0]] 

# Execution - my attempt
def swapLexOrder(str, pairs):
    string = []
    result = ''
    while pairs:
        for letter in str:
            string.append(letter)
        print('original string', string)
        for pair in pairs:
            tupe = tuple(pair)
            string[tupe[1]] = string[tupe[0]]
        print('after swap',string)
    return str

# Refactor/Reflection

def swapLexOrder(str, pairs):
    cycles = list()
    
    for pair in pairs:
        leftcyc = None
        rightcyc = None
        for i in range(len(cycles)):
            if pair[0] in cycles[i]:
                leftcyc = i
            if pair[1] in cycles[i]:
                rightcyc = i
        
        if leftcyc is None:
            leftcyc = len(cycles)   
            cycles.append(set([pair[0]]))
        if rightcyc is None:
            rightcyc = leftcyc
            cycles[rightcyc].add(pair[1]) 
        if leftcyc != rightcyc:
            cycles[leftcyc].update(cycles[rightcyc])
            del cycles[rightcyc]
        
    answer = list(str)
    
    for cycle in cycles:
        letters = []
        for idx in cycle:
            letters.append(str[idx-1])
        letters = sorted(letters, reverse=True)
        cycleidx = sorted(cycle)    
        for i in range(len(cycleidx)):
            answer[cycleidx[i] - 1] = letters[i]
    
    return ''.join(answer)