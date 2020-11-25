
# Execute
def isLucky(n):
    strN = list(str(n))
    length = len(strN)
    middle = length//2
    half1 = strN[:middle]
    half2 = strN[middle:]
    left = 0
    right = 0
    for num1 in half1:
        left += int(num1)
    for num2 in half2:
        right += int(num2)
    return left == right

# Refactor/Reflect
def isLucky(n):
    strN = list(str(n))
    middle = len(strN)//2
    half1, half2 = strN[:middle], strN[middle:]
    left = right = 0
    for num1, num2 in zip(half1, half2):
        left += int(num1)
        right += int(num2)
    return left == right