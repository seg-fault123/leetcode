import math
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # do bfs with multiple starting points (all the points with rotten oranges)
        m, n = len(grid), len(grid[0])
        minutes = [[math.inf]*n for _ in range(m)]

        def bfs():
            current_minute = 0
            m, n = len(grid), len(grid[0])
            q = deque()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        q.append((i, j))
                        minutes[i][j] = 0
            
            while q:
                current_minute += 1
                next_level = []
                while q:
                    curr_i, curr_j = q.popleft()
                    neighborhood = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for diff_i, diff_j in neighborhood:
                        x, y = curr_i + diff_i, curr_j + diff_j
                        if 0 <= x < m and 0 <= y < n and grid[x][y]==1 and minutes[x][y] == math.inf:
                            next_level.append((x, y))
                            minutes[x][y] = current_minute
                
                for point in next_level:
                    q.append(point)


        bfs()
        max_minute = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if minutes[i][j]==math.inf:
                        return -1
                    else:
                        max_minute = max(max_minute, minutes[i][j])
        
        return max_minute


