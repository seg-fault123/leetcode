"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def make_node(start_y, end_y, start_x, end_x):
            required_value = grid[start_y][start_x]
            is_leaf = True
            for i in range(start_y, end_y+1):
                for j in range(start_x, end_x+1):
                    if grid[i][j]!=required_value:
                        is_leaf = False
                        break
                if not is_leaf:
                    break
            new_node = Node(required_value, is_leaf, None, None, None, None)
            if not is_leaf:
                mid_x = (start_x+end_x)//2
                mid_y = (start_y + end_y)//2
                new_node.topLeft = make_node(start_y, mid_y, start_x, mid_x)
                new_node.topRight = make_node(start_y, mid_y, mid_x+1, end_x)
                new_node.bottomLeft = make_node(mid_y+1, end_y, start_x, mid_x)
                new_node.bottomRight = make_node(mid_y+1, end_y, mid_x+1, end_x)
            return new_node
        
        n = len(grid)
        return make_node(0, n-1, 0, n-1)
