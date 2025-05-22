# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_height(root):
            if (not root) or (not root.right and not root.left):
                return 0, 0
            
            left_dim, left_height = diameter_height(root.left)
            right_dim, right_height = diameter_height(root.right)
            height = 1+max(left_height, right_height)

            # if we include the root in the diameter, then then diamter is
            # left height + right height + the two edges that lead to left and right.
            # If edge is not there, then it is not added
            dim = left_height+right_height
            if root.left:
                dim += 1
            if root.right:
                dim += 1
                
            # choose the coice which maximises the diameter
            dim = max(dim, left_dim, right_dim)
            return dim, height
        
        return diameter_height(root)[0]
            
