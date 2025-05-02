# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        ## three conditions:
        ## 1) No child, simply delete the node
        ## 2) 1 child, replace with the child subtree
        ## 3) 2 child, inorder successor, replace the value, and delete the inorder
        ## 4) successor node

        # we use recursion because, deleting current node will require the
        # info of the parent node, which will be accessible in the recusrion stack
        

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if (not root.left) and (not root.right):
                return None
            elif (not root.left) or (not root.right):
                return root.left if root.left else root.right

            replace = root.right
            while replace.left:
                replace = replace.left
            
            root.val = replace.val
            root.right = self.deleteNode(root.right, replace.val)
        
        return root
