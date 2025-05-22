# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = [0]
        # maintain a mapping of values to the index in inorder array
        in_index = {val:index for index, val in enumerate(inorder)}
        def build(in_start, in_end):
            if in_start > in_end:
                return None
            # the current value in preorder array is the node.val
            node = TreeNode(val = preorder[pre_index[0]])
            pre_index[0] += 1

            # update the range for the children
            node.left = build(in_start, in_index[node.val]-1)
            node.right = build(in_index[node.val]+1, in_end)
            return node
            
        root = build(0, len(preorder)-1)

        return root
