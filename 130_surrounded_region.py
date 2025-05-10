class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs only on corner 0's. All the o's not visited afterwards are surrounded
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs_visit(i, j, m, n):
            visited[i][j] = True
            for diff_x, diff_y in diffs:
                x, y = i + diff_x, j + diff_y
                if 0 <= x < m and 0 <= y < n and board[x][y]=='O' and (not visited[x][y]):
                    dfs_visit(x, y, m, n)
            return 

        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs_visit(i, 0, m, n)
            if board[i][n-1] == 'O' and not visited[i][n-1]:
                dfs_visit(i, n-1, m, n)
        for j in range(n):
            if board[0][j] == 'O' and not visited[0][j]:
                dfs_visit(0, j, m, n)
            if board[m-1][j] == 'O' and not visited[m-1][j]:
                dfs_visit(m-1, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and (not visited[i][j]):
                    board[i][j] = 'X'
                


        #normal dfs
        # def dfs(m, n):
        #     for i in range(m):
        #         for j in range(n):
        #             if board[i][j]=='O' and (not visited[i][j]):
        #                 nodes = []
        #                 corner = dfs_visit(i, j, m, n, nodes)
        #                 if not corner:
        #                     for x, y in nodes:
        #                         board[x][y] = 'X'
                    
        
        # def dfs_visit(i, j, m, n, nodes):
        #     visited[i][j] = True
        #     nodes.append((i, j))
        #     corner = False
        #     if i==0 or i==m-1:
        #         corner= True
        #     elif j==0 or j==n-1:
        #         corner=True
        #     for diff_x, diff_y in diffs:
        #         x, y = i + diff_x, j + diff_y
        #         if 0 <= x < m and 0 <= y < n and board[x][y]=='O' and (not visited[x][y]):
        #             corner |= dfs_visit(x, y, m, n, nodes)
            
        #     return corner 
        
        # dfs(m, n)
        # return
