# Understanding
# l = SLL of integers
# k is the value to remove from SLL
# Traverse through SLL and 
# if node.next = k 
# changing next pointer to node.next.next
# return new list
sll = [3, 1, 2, 3, 4, 5]
remove = 3
# Planning
# intialize prev pointer
# while l is not empty:
#   if l.value == k:
#       node.next == node.next.next
#   node = node.next
#   results.append(node)
# return results

# Execute
def removeKFromList(l, k):
    # initialize prev pointer
    prev = None
    # storing SLL in start variable
    start = l
    # while SLL has nodes
    while l != None:
        # check if the nodes value is equal k
        if l.value == k:
            # if prev pointer isn't empty
            if prev != None:
                # set pointer to node ahead of removed node
                prev.next = l.next
            else:
                # else make start the node after removed value
                start = l.next
        else:
            # set prev pointer to new node
            prev = l
        # traverse through SLL
        l = l.next
    # return SLL              
    return start