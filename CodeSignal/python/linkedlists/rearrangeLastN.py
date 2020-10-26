# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# Understanding
# LL of integers
# n as non-negative int 
# based off n value, move the last of those nodes to beginning
# l = [1, 2, 3, 4] | n = 2
# rearrangelastn(l, n) = [2, 3, 4, 1] 


# Plan
# loop thru list, once we find node.value = n
# head_node = ListNode(l.value)
# curr = l
# temp = None
# while curr:
#   if curr.value = n:
#       temp = curr
#   if curr.value != n:
#       curr = curr.next
# temp = node.value = n
# temp_head = temp

# while temp != None:
    # temp = temp.next
    # if temp.next == None:
        # curr = temp
        # curr.next = head_node
        
# n = 2
#                            curr v
# viz = L(1) -> L(2) -> L(3) -> L(4)
#                            temp ^

# Execute my attempt
# def rearrangeLastN(l, n):
#     head_node = ListNode(l.value)
#     curr = l
#     temp = None
#     while curr:
#         if curr = n:
#             temp = curr
#         if curr != n:
#             curr = curr.next
#         temp = node.value = n
#         temp_head = temp

#     while temp != None:
#         temp = temp.next
#         if temp.next == None:
#             curr = temp
#             curr.next = head_node

# if n == 0:
#     return l
# front, back = l, l
# for _ in range(n):
#     front = front.next
# if not front:
#     return l
# while front.next:
#     front = front.next
#     back = back.next
# out = back.next
# back.next = None
# front.next = l
# return out
def rearrangeLastN(l, n):
    if n == 0:
        return l
    front = back = l
    for _ in range(n):
        front = front.next
    if not front:
        return l
    while front.next:
        front = front.next
        back = back.next
    out = back.next
    back.next = None
    front.next = l
    return out