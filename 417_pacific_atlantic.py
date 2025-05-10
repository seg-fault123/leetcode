from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run bfs such that we can reach pacific ocean
        def bfs(visited: set):
            # visited will have the edge points that are can flow their water to ocean
            q = deque()
            for point in visited:
                q.append(point)
            m, n = len(heights), len(heights[0])
            neighborhood = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                curr_x, curr_y = q.popleft()
                for diff_x, diff_y in neighborhood:
                    x, y = curr_x + diff_x, curr_y + diff_y
                    if 0 <= x < m and 0 <= y < n and ((x, y) not in visited) and heights[curr_x][curr_y] <= heights[x][y]: # makes sure that water can go from x, y to curr_x, curr_y
                        visited.add((x, y))
                        q.append((x, y))
                    
            return visited
        

        m, n = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        # add edge points
        for i in range(m):
            pacific_visited.add((i, 0))
            atlantic_visited.add((i, n-1))
        # add edge points
        for j in range(n):
            pacific_visited.add((0, j))
            atlantic_visited.add((m-1, j))
        # for pacific
        pacific_visited = bfs(pacific_visited)
        # for atlantic
        atlantic_visited = bfs(atlantic_visited)
        
        return list(pacific_visited.intersection(atlantic_visited))
