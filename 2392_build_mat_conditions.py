class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # if u comes above v or u comes at left of v, then v's position depends on u's position. And there is an edge from v to u

        def make_adj_list(k, conditions):
            adj_list = [[] for _ in range(k)]
            # before considering v, consider u
            for u, v in conditions:
                adj_list[v-1].append(u-1)
            return adj_list
        
        def topological_sort(k, adj_list, result):
            # builds the result. result[i] is the position that the ith node takes in the topo sort
            visited = [0]*k
            def dfs_visit(node, result):
                if visited[node]==2:
                    return True
                
                visited[node] = 1
                for neighbor in adj_list[node]:
                    if visited[neighbor]==1 or not dfs_visit(neighbor, result):
                        return False
                
                visited[node] = 2
                result[node] = len(result) # position/index of node is equal to the number of nodes that have already been included before the current node
                return True

            for i in range(k):
                if visited[i]==0 and not dfs_visit(i, result):
                    return False
            return True

            
        
            
        adj_list = make_adj_list(k, rowConditions)
        row_node_positions = {}
        # build row_node_positions
        # row_node_positions[i] gives the row index of the ith node
        if not topological_sort(k, adj_list, row_node_positions):
            # topo sort was not possible
            return []
        
        # build for columns
        adj_list = make_adj_list(k, colConditions)
        col_node_positions = {}
        if not topological_sort(k, adj_list, col_node_positions):
            return []
        
        result = [[0]*k for _ in range(k)]
        for i in range(k):
            result[row_node_positions[i]][col_node_positions[i]] = i+1 # the actual number of node, we used i-1 as the node value throughout
        
        return result
