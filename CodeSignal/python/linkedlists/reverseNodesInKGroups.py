# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

# Understanding
# take a LL and reverse nodes by 'k' value at a time
# return modified list
# if number is not multiple of k, leave nodes alone
# o(n) time complexity / o(1) space complexity
# if idx % k == 0 
# reverse node = change it's next pointer to kth node previous
#             prev v
# ex: k = 2 | l = [1, 2, 3, 4]
#                curr ^
# counter = 4
#                         prev v
#    L(2) -> L(1) -> L(4) -> L(3)
#                         curr ^
# nsn  ^
# Planning
# def revnodesinkgroups(LL, k):
    # head_node = LL.value
    # curr, prev = head_node, head_node
    # counter = 4
    
    # while curr.next:
        # if counter % k == 0:
            # prev.next, curr.next = curr.next, prev
            # if counter == k:
                # new_start_node = curr
            # curr = prev
            # while prev.next != None:
                # prev = prev.next
        # while curr.next != None:
            # curr = curr.next
            # counter += 1
        
    # return new_start_node
    


# Execute my attempt 1 hour
# def reverseNodesInKGroups(l, k):
#     head_node = ListNode(l.value)
#     curr, prev, new_start_node = head_node, head_node, head_node
#     counter = 1
#     while curr.next:
#         if counter % k == 0:
#             prev.next, curr.next = curr.next, prev
#             if counter == k:
#                 new_start_node = curr
#             curr = prev
#             while prev.next != None:
#                 prev = prev.next
#         curr = curr.next
#         counter += 1
#     return l

def reverseNodesInKGroups(l, k):
    if not l:
        return l
    curr = l
    n = k
    while curr and n:
        curr = curr.next
        n -= 1
    if n:
        return l
    curr, prev, next, n = l, None, None, k
    while curr and n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n -= 1
    if next:
        l.next = reverseNodesInKGroups(next, k)
    return prev