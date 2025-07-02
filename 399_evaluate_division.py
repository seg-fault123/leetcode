from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # in equations[i] a/b translates to a->b edge with weight values[i]
        # similarly b/a will have a weight 1/values[i]
        # path a->b->c will give a/c, weights will be multiplied to find the value of the path


        # one more solution exists where we apply floyd warshall and calculate all possible paths from all sources and store their value. This will perform better when there are a large number of queries.

        
        adj_list = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a in adj_list:
                adj_list[a][b] = values[i]
            else:
                adj_list[a] = {b: values[i]}
            if b in adj_list:
                adj_list[b][a] = 1/values[i]
            else:
                adj_list[b] = {a: 1/values[i]}


        def bfs(source, dest):
            q = deque()
            q.append((source, 1))
            visited = {node: False for node in adj_list}
            visited[source] = True
            while q:
                node, val = q.popleft()
                for neighbor, weight in adj_list[node].items():
                    if neighbor==dest:
                        return val*weight
                    if not visited[neighbor]:
                        q.append((neighbor, val*weight))
                        visited[neighbor] = True
            
            return -1
        
        result = []
        for a, b in queries:
            if (a not in adj_list) or (b not in adj_list):
                result.append(-1)
            elif a==b:
                result.append(1)
            else:
                result.append(bfs(a, b))
        
        return result
        
