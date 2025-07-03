class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        # the idea is to remove all those nodes that have a degree of 1 (leaves). Atleast one leaf will always exist
        # non-leaf nodes which are adjacent to a leaf node is a better candidate to be a root than the leaf, because all paths to other nodes will have 1 less edge when calculated from this non-leaf node when compared to the leaf node. So remove all leaf nodes until the graph has only leaf nodes n==1 or n==2
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        leaves = [i for i in range(n) if len(adj_list[i])==1]
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop() # this leaf will only have 1 neighbor
                adj_list[neighbor].remove(leaf) # delete the leaf
                if len(adj_list[neighbor])==1:
                    # check if the neighbor becomes a leaf
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves
