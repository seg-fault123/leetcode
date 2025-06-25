import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # we'll maintain 2 heaps, one to track the available rooms, another to track the ongoing meetings
        meetings.sort(key=lambda x: x[0])
        counts = [0]*n
        available = list(range(n))
        current_meetings = []

        for meeting in meetings:
            # if some ongoing meeting ended before this meeting then its room can be allocated to it. Make those rooms available
            while current_meetings and current_meetings[0][0] <= meeting[0]:
                end, room = heapq.heappop(current_meetings)
                heapq.heappush(available, room)
            # if a room is available, the assign that room to it
            if available:
                room = heapq.heappop(available)
                counts[room] += 1
                # structure is end, room
                meeting[0], meeting[1] = meeting[1], room
                heapq.heappush(current_meetings, meeting)
            else:
                # if not available, then see when the next meeting will end, assign it that room, moreover update the end time of the current meeting
                end, room = heapq.heappop(current_meetings)
                meeting[1] = end + meeting[1]-meeting[0]
                counts[room]+=1
                meeting[0], meeting[1] = meeting[1], room
                heapq.heappush(current_meetings, meeting)
        
        # find the room with max uses
        result, result_room = counts[0], 0
        for i in range(1, n):
            if result < counts[i]:
                result = counts[i]
                result_room = i
        return result_room
