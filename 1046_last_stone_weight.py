import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapq.heapify(heap)
        while heap:
            weight1 = -heapq.heappop(heap)
            if not heap:
                return weight1
            weight2 = -heapq.heappop(heap)
            if weight1!=weight2:
                heapq.heappush(heap, weight2-weight1)
        
        return 0
