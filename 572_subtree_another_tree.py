# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# another solution at  https://leetcode.com/problems/subtree-of-another-tree/solutions/102741/python-straightforward-with-explanation-o-st-and-o-s-t-approaches/
# merkle hash (more otimal than this code)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subtree(root, subroot, matched):
            if not root:
                return not subroot
            elif not subroot:
                return False
        
            if root.val == subroot.val and subtree(root.left, subroot.left, True) and subtree(root.right, subroot.right, True):
                return True
        
            elif not matched:
                return subtree(root.left, subroot, False) or subtree(root.right, subroot, False)
            
            else:
                return False
        
        return subtree(root, subRoot, False)
