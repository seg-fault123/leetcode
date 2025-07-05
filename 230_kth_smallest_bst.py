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

        # follow up question.
        # if we make a tree such that the node contains additional information of maintaining how many nodes are there in the sub tree rooted at that node. So num nodes in the left tree + num numdes in the right tree + 1 (itself). Then the complexity changes to O(h) where h is the height of the tree.
        # if the left tree contains more than k elements, we search the kth smallest element in left subtree
        # if the left subtree contains k-1 elements, the current node contains the kth smallest element
        # if left+1 < k, then search for (k-left-1)th element in the right subtree
        # each time we only search in the correct half of the tree

        # if root is None:
        #     return None
        
        # left_count = left.count if left else 0
        # if left_count >= k:
        #     return kth(left, k)
        
        # elif left_count+1 == k:
        #     return node.val
        # else:
        #     return kth(right, k-left.count-1)
    
