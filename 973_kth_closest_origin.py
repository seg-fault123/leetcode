import heapq

class Point:
    def __init__(self, point):
        self.point = point
        self.distance = -(point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [Point(point) for point in points]
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        return [point.point for point in points]
        
