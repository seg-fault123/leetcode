# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## the first node such that p and q are not on the same side of itself is
        # the LCA
        while root:
            if p.val < root.val and q.val < root.val: ## both p and q are on left
                root = root.left
            elif p.val > root.val and q.val > root.val: ## both p and q are on right
                root= root.right
            else:
                return root



        # ## efficient version of the below algorithm which finds p and q 
        # if not root or root==p or root==q:
        #     # cases where none is encountered or p or q is found
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     # case where root is neither p nor q but both left and right have atleast 1
        #     return root
        
        # # propogate whatever was found to the upper levels
        # return left if left else right



        # def _lca(root, p, q):
        #     if not root:
        #         return False, False, None
            
        #     found_p = False
        #     found_q = False

        #     found_pl, found_ql, lca = _lca(root.left, p, q)
        #     if lca:
        #         return found_pl, found_ql, lca
        #     found_pr, found_qr, lca = _lca(root.right, p, q)
        #     if lca:
        #         return found_pr, found_qr, lca
        #     found_p, found_q = found_pr or found_pl, found_qr or found_ql 
        #     if p.val == root.val:
        #         found_p = True
        #     if q.val == root.val:
        #         found_q = True
        #     if found_p and found_q:
        #         lca = root
        #     return found_p, found_q, lca

        # return _lca(root, p, q)[2]
