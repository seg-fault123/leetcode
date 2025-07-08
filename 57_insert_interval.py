class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search(target, index):
            start = 0
            end = len(intervals)-1
            while start <= end:
                mid = (start+end)//2
                if intervals[mid][index] == target:
                    return mid
                elif intervals[mid][index] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                
            return start
        
        # find the correct positions wrt the start and end time
        start = binary_search(newInterval[0], 0)
        end = binary_search(newInterval[1], 1)

        # check if overlap with previous
        if start > 0:
            prev = intervals[start-1]
            if newInterval[0] <= prev[1]:
                newInterval[0] = prev[0]
                start -= 1

        # check if overlap with next
        if end < len(intervals):
            next_i = intervals[end]
            if next_i[0] <= newInterval[1]:
                newInterval[1] = next_i[1]
                end += 1
        
        return intervals[:start] + [newInterval] + intervals[end: ]
        
