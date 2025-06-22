class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # do one dive of dfs, no cycles should be detected and every 
        # node should be visited after the dive
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False]*n

        # return True when no cycle is detected
        # parent is also passed so that dfs on parent is not called again, otherwise
        # in an undirected graph since both (u, v) and (v, u) are stored, it might
        # incorrectly recognize this as a cycle
        def dfs(node, parent):
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in adj_list[node]:
                if neighbor!=parent and not dfs(neighbor, node):
                    return False
            return True
        
    
        if not dfs(0, n):
            # cycle was detected
            return False
            
        # check that all nodes should be visited    
        for visit in visited:
            if not visit:
                return False
        return True
                

