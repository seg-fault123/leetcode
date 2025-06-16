from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # result = []
        # q = deque()
        # q.append((root, 0))
        # while q:
        #     node, level = q.popleft()
        #     if not node:
        #         continue
        #     if len(result)==level:
        #         result.append([node.val])
        #     else:
        #         result[level].append(node.val)
        #     if node.left:
        #         q.append((node.left, level+1))
        #     if node.right:
        #         q.append((node.right, level+1))
        
        # return result

        if root is None:
            return []
        
        result = []
        q = [root]
        while q:
            new_level = []
            curr_level = []
            for node in q:
                curr_level.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            q = new_level
            result.append(curr_level)
        
        return result

        
