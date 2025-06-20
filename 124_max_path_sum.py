
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        # dfs will return max path sum including the root and not splitting
        # if it were to split, we update the result directly
        # if negative comes from bottom, we ignore that and replace with 0
        def dfs(node):
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            split_here = left + right + node.val
            result[0] = max(result[0], split_here)
            return max(left, right) + node.val
        
        dfs(root)
        return result[0]

