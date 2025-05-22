# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        def inorder(root):
            if root is None:
                return None
            
            left = inorder(root.left)
            if left:
                return left
            
            count[0] += 1
            if count[0] == k:
                return root
            
            right = inorder(root.right)
            return right
        
        return inorder(root).val
    
            
            
            
            
            
