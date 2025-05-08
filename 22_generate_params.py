class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(open_num, close_num, current):
            if open_num + close_num == 2*n:
                result.append(current)
                return

            if open_num < n:
                dfs(open_num + 1, close_num, current+'(')
            if close_num < open_num:
                dfs(open_num, close_num+1, current+')')


        dfs(0, 0, '') 
        return result       
