import heapq
import math

# we will use Djikstras algo. We keep two grids to maintain visit and distance information
# If we find a better solution for a cell, instead of updating the key in the heap we
# will just add the cell with the new key in the heap. For this reason we need the 
# distnace grid

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        visited = [[False]*n for _ in range(m)]
        distance = [[math.inf]*n for _ in range(m)]
        distance[0][0] = 0
        heap = [(0, 0, 0)]
        while len(heap) > 0:
            current_effort, current_r, current_c = heapq.heappop(heap)
            prev_effort = distance[current_r][current_c]
            if current_effort > prev_effort: # this happens when two paths are found
            # and the better path has already been popped, outdated entry.
                continue
            if current_r == m-1 and current_c == n-1:
                return current_effort

            visited[current_r][current_c] = True

            adj_diff = [[-1, 0], [1, 0], [0, -1], [0, 1]] # for neighbors
            for dr, dc in adj_diff:
                new_r, new_c = current_r+dr, current_c+dc
                if 0 <= new_r < m and 0 <= new_c < n and (not visited[new_r][new_c]):
                    new_effort = max(current_effort, 
                                        abs(heights[current_r][current_c] - 
                                            heights[new_r][new_c]))
                    if distance[new_r][new_c] > new_effort:
                        distance[new_r][new_c] = new_effort
                        heapq.heappush(heap, (new_effort, new_r, new_c))
        
