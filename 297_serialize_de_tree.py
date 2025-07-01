# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # returns the level order traversal separated by commas and nulls to mark an end of branch
        if root is None:
            return ''

        q = deque()
        q.append(root)
        bfs = ''
        while q:
            node = q.popleft()
            if node:
                bfs += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                bfs += 'null'
            
            if q:
                bfs += ','
        
        bfs = bfs.strip(',null')
        # print(bfs)
        return bfs




    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=='':
            return None
        
        data_list = data.split(',')
        node_list = []
        for i, val in enumerate(data_list):
            if val=='null':
                continue
            new_node = TreeNode(int(val))
            if i>0:
                # connect with the parent node
                parent_index = (i-1)//2
                if parent_index*2 + 1 == i:
                    node_list[parent_index].left = new_node
                else:
                    node_list[parent_index].right = new_node

            node_list.append(new_node)

        return node_list[0]        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
