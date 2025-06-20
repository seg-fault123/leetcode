# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def robbery(node, can_include):
            if node is None:
                return 0
            elif (node, can_include) in memo:
                return memo[(node, can_include)]
            
            if not can_include:
                result = robbery(node.left, True) + robbery(node.right, True)
                memo[(node, False)] = result
                return result
            else:
                skip = robbery(node, False)
                include = node.val + robbery(node.left, False) +  robbery(node.right, False)
                result = max(skip, include)
                memo[(node, True)] = result
                return result
        
        return robbery(root, True)
