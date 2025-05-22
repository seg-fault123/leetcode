# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def count_nodes(root, max_val):
            if root is None:
                return
            if root.val >= max_val:
                count[0] += 1
                max_val = root.val
            
            count_nodes(root.left, max_val)
            count_nodes(root.right, max_val)
        
        count_nodes(root, -math.inf)
        return count[0]
        
