# Understanding
# SLL1, SLl2 as arguments
# return combined into 1 SLL sorted in non-decreasing order
# when combining list, change pointers to appropriate
# node if l1 node > or < l2 node


# (20) -> (19) -> (18) -> (17) -> (16) -> null


# (20) -> (19) -> (18) -> (17) -> (16) -> null

# Planning


# Execution
def mergeTwoLinkedLists(l1, l2):
    head_node = ListNode(None)
    curr = head_node
    while l1 and l2:
        if l1.value <= l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    return head_node.next

# Reflection