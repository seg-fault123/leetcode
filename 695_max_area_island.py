class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs():
            m, n = len(grid), len(grid[0])
            visited = [[False]*n for _ in range(m)]
            max_area = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and (not visited[i][j]):
                        area = dfs_visit(i, j, visited)
                        max_area = max(max_area, area)
            
            return max_area
        
        def dfs_visit(i, j, visited):
            m, n = len(grid), len(grid[0])
            visited[i][j] = True
            area = 1
            difference = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for p, q in difference:
                new_r, new_c = i+p, j+q
                if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c] and (not visited[new_r][new_c]):
                    area += dfs_visit(new_r, new_c, visited)
            return area
        
        return dfs()
