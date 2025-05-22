class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j, m, n, current):
            # the function assumes that all characters of current matches word
            curr_len = len(current)

            # if adding this character will make current and word same
            if curr_len + 1 == len(word):
                return board[i][j] == word[-1]

            # if adding this character will make current and word different 
            elif board[i][j] != word[curr_len]:
                return False
            
            # if code code reaches this step, it means that adding this character will make the initials of current and word same but more chracters have to be checked as the length of word is still larger. So we check the neighbors of this cell
            current += board[i][j]
            visited[i][j] = True
            for diff_x, diff_y in diffs:
                x, y = i+diff_x, j+diff_y
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    if dfs(x, y, m, n, current):
                        return True
                        
            # make this cell available to later searches
            visited[i][j]=False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, m, n, ''):
                    return True
        return False
                
