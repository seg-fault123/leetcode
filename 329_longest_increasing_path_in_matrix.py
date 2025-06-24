class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = [0]

        dp = [[0]*n for _ in range(m)]
        diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, m , n):
            # if dp is greater than 0, it has already been visited and set
            if dp[i][j]:
                return
            for diff_x, diff_y in diffs:
                x, y = i+diff_x, j+diff_y
                # only proceed to those neighbors whose value is strictly greater than the current node, cycles not possible as a visited node in the stack is strictly smaller than the current node and we are only proceeding in the increasing path.
                if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[i][j]:
                    dfs(x, y, m, n)
                    dp[i][j] = max(dp[i][j], dp[x][y])

            dp[i][j] += 1
            result[0] = max(result[0], dp[i][j])
            return
        
        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    dfs(i, j, m, n)
        
        return result[0]
                

        
