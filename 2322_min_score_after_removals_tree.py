class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # For each node i, we store the XOR value of the subtree rooted at i
        # we choose a pair of edge to delete let it be a, b and c, d, let a and c be the lower nodes.
        # let V be the xor of all values
        # if a is ancestor of c:
        #   the three nodes have the values : V^val[a], val[a]^val[c], val[c]
        # elif c is ancestor of a:
        #   the three nodes have the values : V^val[c], val[a]^val[c], val[a]
        # else both a and c are independent:
        #   the three nodes have the values : V^val[a]^val[c], val[a], val[c]

        # array that contains xor_vals of subtree rooted at i
        xor_vals = nums[:]

        adj_list = defaultdict(list)
        
        descendents = defaultdict(set)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = [False]*len(nums)
        
        def dfs(node):
            visited[node] = True

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    # neighbor is not yet visited then make it the descendent of the current node
                    descendents[node].add(neighbor)
                    dfs(neighbor)
                    # add the descendents of the neighbor to the descendents of current node, same for xor_vals
                    descendents[node] |= descendents[neighbor]
                    xor_vals[node] ^= xor_vals[neighbor]
            
            return xor_vals[node]
        
        # call dfs on any index, as the graph is connected, total_xor will be returned
        total_xor = dfs(0)
        result = float('inf')
        for i in range(len(edges)-1):
            for j in range(i+1, len(edges)):
                a, b = edges[i]
                if b in descendents[a]:
                    a, b = b, a
                
                c, d = edges[j]
                if d in descendents[c]:
                    c, d = d, c

                curr = None
                if a in descendents[c]:
                    curr = [total_xor^xor_vals[c], xor_vals[c]^xor_vals[a], xor_vals[a]]
                elif c in descendents[a]:
                    curr = [total_xor^xor_vals[a], xor_vals[c]^xor_vals[a], xor_vals[c]]
                else:
                    curr = [total_xor^xor_vals[c]^xor_vals[a], xor_vals[c], xor_vals[a]]
                
                result = min(result, max(curr)-min(curr))
            
        
        return result
