class Solution:
    # one more solution exists where instead of marking the individual coordinated, we mark the diagonals that are being used.

    def totalNQueens(self, n: int) -> int:
        result = [0]
        visited = [[False]*n for _ in range(n)]

        def mark_visit(i, j, n):
            visited[i][j] = True
            marked_list = [[i, j]]

            for p in range(1, n-i):
                diffs = [[i+p, j], [i+p, j-p], [i+p, j+p]]
                for x, y in diffs:
                    if 0<=x<n and 0<=y<n and not visited[x][y]:
                        visited[x][y] = True
                        marked_list.append([x, y])
            
            return marked_list
        
        def mark_free(marked_list):
            for x, y in marked_list:
                visited[x][y] = False
        

        def dfs(index, n):
            if index==n:
                result[0] += 1
                return
            
            for col in range(n):
                if not visited[index][col]:
                    marked_list = mark_visit(index, col, n)
                    dfs(index+1, n)
                    mark_free(marked_list)
        
        dfs(0, n)
        return result[0]


