import heapq
import math
# djikstra algo with path cost being the max value of an intermediate node instead of the sum of the nodes.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distances = {(i, j):math.inf for i in range(n) for j in range(n)}
        distances[(0, 0)] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        diffs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while heap:
            curr_dist, x, y = heapq.heappop(heap)
            if distances[(x,y)] < curr_dist:
                continue
            if x==n-1 and y==n-1:
                return curr_dist
            for diff_x, diff_y in diffs:
                new_x , new_y = x + diff_x, y + diff_y
                if 0<=new_x<n and 0<=new_y<n:
                    new_distance = max(curr_dist, grid[new_x][new_y])
                    if new_distance < distances[(new_x, new_y)]:
                        distances[(new_x, new_y)] = new_distance
                        heapq.heappush(heap, (new_distance, new_x, new_y))

        return distances[(n-1, n-1)]
        
