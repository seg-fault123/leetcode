class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search(arr, target, index):
            start = 0
            end = len(intervals) - 1
            while start <= end:
                mid = (start + end)//2
                mid_interval = intervals[mid]
                if mid_interval[index] == target:
                    return mid
                elif mid_interval[index] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start 
        
        # find the correct positions wrt the start and end time
        start = binary_search(intervals, newInterval[0], 0)
        end = binary_search(intervals, newInterval[1], 1)
        
        # check if overlap with previous
        if start > 0:
            prev_interval = intervals[start-1]
            if prev_interval[0] <= newInterval[0] <= prev_interval[1]:
                newInterval[0] = prev_interval[0]
                newInterval[1] = max(prev_interval[1], newInterval[1])
                start -= 1

        # check if overlap with next
        if end < len(intervals):
            next_interval = intervals[end]
            if next_interval[0] <= newInterval[1] <= next_interval[1]:
                newInterval[1] = next_interval[1]
                end += 1

        # append the results
        result = []
        for i in range(start):
            result.append(intervals[i])
        result.append(newInterval)
        for i in range(end, len(intervals)):
            result.append(intervals[i])
        return result 


        
