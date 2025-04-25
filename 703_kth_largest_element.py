import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
        

# maintain atmost k elements in the heap. The element at the top of the min heap is the
# kth largest element of the list. If a new element is there which is larger than the current
# kth largest element, then the top will be removed and this new element will be pushed as the
# kth largest element needs to be updated. The heap remains unchanged otherwise.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
