class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [[0, 0] for _ in range(n)] # for each number [outdegree, indegree], if a trusts b then there is an edge from a to b
        for a, b in trust:
            degrees[a-1][0] += 1
            degrees[b-1][1] += 1
        
        # to check if a town judge exists, its outdegree should be 0 as it trusts no one and its indegree should be n-1 as it is trusted by all the others
        for i in range(n):
            if degrees[i][1]==n-1:
                return i+1 if degrees[i][0]==0 else -1
        
        return -1
