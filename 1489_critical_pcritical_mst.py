class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
            
            def find(self, u):
                while u!=self.parent[u]:
                    self.parent[u] = self.parent[self.parent[u]]
                    u = self.parent[u]
                return u
            
            def union(self, u, v):
                u_root = self.find(u)
                v_root = self.find(v)
                if v_root != u_root:
                    self.parent[v_root] = u_root
                    return True
                else:
                    return False
        # add the original index to produce the result
        for i in range(len(edges)):
            edges[i].append(i)
            
        edges.sort(key = lambda x: x[2])

        def kruskal(n, include=None, skip=-1):
            disjoint = UnionFind(n)
            mst_weight = 0
            count_edges = 0
            # if include then include
            if include:
                u, v, weight, _= edges[include]
                mst_weight += weight
                count_edges += 1
                disjoint.union(u, v)
            
            for i in range(len(edges)):
                # if skip then skip
                if i==skip:
                    continue
                
                u, v, weight, _ = edges[i]
                if disjoint.union(u,v):
                    mst_weight += weight
                    count_edges += 1
                    # if tree is already formed
                    if count_edges==n-1:
                        break
            
            return mst_weight if count_edges==n-1 else float('inf')
        
        original_mst = kruskal(n)

        critical = []
        pseudo = []

        for i in range(len(edges)):
            u, v, w, prev_index = edges[i]
            skip_weight = kruskal(n, skip=i)
            # if skippinf edge i leads to a worse mst then edge is critical
            if skip_weight > original_mst:
                critical.append(prev_index)
            else:
                # if including edge i leads to same mst then edge i is pseudo critical 
                include_weight = kruskal(n, include=i)
                if include_weight==original_mst:
                    pseudo.append(prev_index)
        
        return [critical, pseudo]
            

