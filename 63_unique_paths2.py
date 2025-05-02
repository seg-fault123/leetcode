class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        result = [[0]*n for _ in range(m)]
        result[0][0] = 1 if obstacleGrid[0][0]==0 else 0
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                result[i][0] = result[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                result[0][j] = result[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]
