class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Eulerian path, 
        graph = {}
        order = [] # reverse of order is the answer
        for start, end in sorted(tickets, reverse=True):
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]
            if end not in graph:
                graph[end] = []
        
        def dfs(current_place):
            if not graph[current_place]:
                # if a deadend, just append to the order (works somehow)
                order.append(current_place)
                return
            
            while graph[current_place]:
                dfs(graph[current_place].pop())
            order.append(current_place)
            return
        
        dfs('JFK')
        return order[::-1]

        # Time limit exceeded, dfs till we find first solution
        # result = []
        # graph = {}
        # for start, end in tickets:
        #     if start in graph:
        #         graph[start].append(end)
        #     else:
        #         graph[start] = [end]
        #     if end not in graph:
        #         graph[end] = []
        # for start in graph:
        #     graph[start].sort()
        
        # def dfs(current_place, graph, num_tickets, order):
        #     if num_tickets == len(tickets):
        #         result.append(order)
        #         return 
        #     if len(graph[current_place])==0:
        #         return
            
        #     neighbors = graph[current_place]
        #     for i, neighbor in enumerate(neighbors):
        #         graph[current_place] = neighbors[:i] + neighbors[i+1:]
        #         dfs(neighbor, graph, num_tickets+1, order+[neighbor])
        #         if result:
        #             return
        #         graph[current_place] = neighbors
            
        #     return
        
        # dfs('JFK', graph, 0, ['JFK'])
        # return result[0]

            
            
