class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parent[0] will not be used since nodes start with 1
        parent = [i for i in range(len(edges)+1)]

        # find with path compression
        def find(u):
            # root is that node whose parent is itself
            # until you reach the root, update the pointers to reduce the path to reach the root
            while parent[u]!=u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            
            return u

        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if v_root != u_root:
                parent[v_root] = u_root
                return True
            else:
                return False
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
