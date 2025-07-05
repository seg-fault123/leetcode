"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda x: x.start)
        # if there is a conflict between any intervals, then current interval will have to be
        # scheduled the next day. So no matter if the next intervals do not have any conflicts between
        # one another and previous intervals,  two days will still be required for the scheduling.

        # heap is a min heap that holds the end times of the previous intervals.
        # the length of the heap tells that those many-1 simultaneous conflicts have been encountered in the past. Even if the
        # current intervals in the heap do not conflict. So len(heap) many days will atleast be required to schedule meetings
        for interval in intervals:
            # check if the current interval has a conflict with the earliest ending meeting in the heap. If it does, then it has
            # conflict with all other intervals in the heap as all other meetings have end time greater than top. So just push the end time in the heap
            # to represent that one more day will be required. Once a heap reaches a length, it maintains it. So, in th end the length of the heap
            # tells us that those many days will atleast be required
            if heap and heap[0]<=interval.start:
                # if the meeting does not conflict with the earliest (top) meeting, then we can think of it beeing alloted in the same day
                # as the top meeting, so pop, the earliest meeting and insert the current meeting.
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        
        return len(heap)
