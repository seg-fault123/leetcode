import heapq
import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algo
        def distance(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        distances = {(x, y): math.inf for x, y in points}
        not_visited = set([(x, y) for x, y in points])
        cost = 0

        heap = [(0, tuple(points[0]))]
        distances[tuple(points[0])] = 0
        while heap:
            current_distance, current_point = heapq.heappop(heap)
            # outdated entry
            if distances[current_point] < current_distance:
                continue

            cost += current_distance
            not_visited.remove(current_point)
            for  other in not_visited:
                new_distance = distance(other, current_point)
                if new_distance < distances[other]:
                    distances[other] = new_distance
                    heapq.heappush(heap, (new_distance, other))

        return cost 
