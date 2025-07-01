import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        max_heap = []
        i = 0
        array = sorted((capital[i], profits[i]) for i in range(n))
        while k > 0:
            # push all the projects in the heap which can be done
            while i<n and array[i][0] <= w:
                heapq.heappush(max_heap, -array[i][1])
                i += 1
            
            if not max_heap:
                # no values left in the heap, cannot do more projects
                break
            
            w += -heapq.heappop(max_heap) # add the profit
            k -= 1
        
        return w
        


