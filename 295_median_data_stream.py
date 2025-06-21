import heapq
class MedianFinder:
# half elements are stored in max_heap of smaller numbers.
# half elements are stored in min_heap of bigger numbers
# if max heap is allowed to have 1 extra element
    def __init__(self):
        self.max_heap = []
        self.min_heap = []        

    def addNum(self, num: int) -> None:
        if not self.min_heap or num <= self.min_heap[0]:
            # num is equal or smaller than all elements in minheap
            heapq.heappush(self.max_heap, -num)
            # if length constraints are violated then transfer numbers
            if len(self.max_heap) > len(self.min_heap)+1:
                element = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, element)
        else:
            # num is greater than all elements in max_heap
            heapq.heappush(self.min_heap, num)
            # if length constraints are violated then transfer numbers
            if len(self.max_heap) < len(self.min_heap):
                element  = -heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, element)
        
        

    def findMedian(self) -> float:
        # since max heap is allowed to have 1 extra element, if max_heap has higher length, the median is top of max_heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            # else both max_heap and min_heap have rthe same length, take the mean of the respective top elements
            return (-self.max_heap[0] + self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
