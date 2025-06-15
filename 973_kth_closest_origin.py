import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            if len(heap) < k or heap[0][0] < -distance:
                heapq.heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x,  y] for _, x, y in heap]  
        
