# Understanding
# Given 2 LL's w/ numbers that are 4 digits
# a represented number may have leading zeros
# return result in same format (LL)
# if length of SLL for a/b is equal, then 
# add up corresponding nodes
# if not, join integers in SLL together and 
# add each total value together
# parse by 4 digits each 

# Planning
# intialize results arr
# total = []
# anum = []
# bnum = []
# while a != None:
#   anum.append(a.value)
#   a = a.next
# while b != None:
#   bnum.append(b.value)
#   b = b.next
# aint = "".join(anum)
# bint = "".join(bnum)
# result = aint + bint
# total.append(result)

# Executing
def addTwoHugeNumbers(a, b):
    total = []
    anum = []
    bnum = []
    while a != None:
        anum.append(a.value)
        a = a.next
    while b != None:
        bnum.append(b.value)
        b = b.next
    carry = 0
    while anum or bnum: 
        resultVal = (anum.pop() if anum else 0) + (bnum.pop() if bnum else 0) + carry
        total.append(resultVal % 10000)  
        carry = resultVal // 10000
    if carry:
        total.append(carry)   
    res = ListNode(0)
    r = res
    while total:
        r.next = ListNode(total.pop())
        r = r.next
    return res.next


# Reflect/Refactor