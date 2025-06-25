import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1]*len(queries)
        start = 0
        interval_heap = []
        # the basic idea is that to sort the elements and queries in ascending order
        # when processing a query add all those intervals which have left less than equal to query to a heap. The heap structure is [size, end]. So 
        intervals.sort()
        queries = sorted([(q, index) for index, q in enumerate(queries)])
        for query, index in queries:
            while start < len(intervals) and intervals[start][0] <= query:
                interval = intervals[start]
                interval[0]= interval[1]-interval[0]+1
                heapq.heappush(interval_heap, interval)
                start += 1
            
            # now check if there are small intervals whose right values are smaller than query and remove them as no other query will be contained in such intervals
            while interval_heap and interval_heap[0][1] < query:
                heapq.heappop(interval_heap)
            
            # only those intervals were added whose left is smaller or equal to q. And all those intervals which were smaller and did not contain query were removed. The heap may still contain large intervals which do not contain query but they definitely are not the heaps top element.
            if interval_heap:
                result[index] = interval_heap[0][0]
            
        return result

        
