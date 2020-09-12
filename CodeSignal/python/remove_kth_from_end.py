# k = 2

# length = 5
# count = 3
#  h_n    h.nxt
# (20) -> (19) -> (18) -> (17) -> (16) -> null

def remove_kth_from_end(head, k):
    # initialize counters
    length = 1
    count = 1
    # preserving head in head_node variable
    # (20)
    head_node = head
    # while loop to measure length of SLL
    while head_node.next:
        length += 1
        head_node = head_node.next
    # reset head_node to (20)
    head_node = head
    # edge case test 5
    if length == k:
        return head.next
    while count < length-k:
        count += 1
        head_node = head_node.next
    return head

# R
# while count == length-k:
#   set head_node.next = head_node.next.next
# this removes the node from the SLL because there is no longer
# a pointer to that node

