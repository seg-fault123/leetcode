class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')]*n
        dist[src] = 0
        # initially every distance is inf except dist[src], which is zero.
        # bellman ford is applied k+1 times to determine the shortest path with at most k nodes in between (excluding both endpoints)
        # relax fist time gives shortest path for k=0
        # relaxing 2nd time gives shortest path for k=1
        # relaxing k+1 time gives shortest path for k 
        for _ in range(k+1):
            temp = dist[:]
            for from_loc, to_loc, price in flights:
                temp[to_loc] = min(temp[to_loc], dist[from_loc]+price)
            dist = temp

        return -1 if dist[dst]==float('inf') else dist[dst]



