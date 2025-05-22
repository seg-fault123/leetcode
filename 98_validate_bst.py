# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_range(min_val, max_val, root):
            if root is None:
                return True
            
            if min_val < root.val < max_val:
                return valid_range(min_val, root.val, root.left) and valid_range(root.val, max_val, root.right)
            else:
                return False
        
        return valid_range(-math.inf, math.inf, root)
        
