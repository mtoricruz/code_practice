# Understanding 
# preorder traversal - BFS
# 0th index of preorder list is root
    # left of root in Inorder list is left subtree
    # right of root in Inorder list is right subtree
# [:right of leaf node in preorder] is right subtree
# restore tree node(t)
    # t.right = nodes.remove(1,1)
    # t.left = nodes.remove(0,1)

# Planning
#

# Execution
# def restoreBinaryTree(inorder, preorder):

# Refactor/Reflection:
def restoreBinaryTree(inorder, preorder):
    if not preorder:
        return None
    root = Tree(preorder[0])
    i = inorder.index(preorder[0])
    root.left = restoreBinaryTree(inorder[:i], preorder[1:i+1])
    root.right = restoreBinaryTree(inorder[i+1:], preorder[i+1:])
    return root