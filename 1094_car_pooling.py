import heapq
# another solution at https://leetcode.com/problems/car-pooling/solutions/390356/most-simple-solution-o-n-10-lines-with-explanation-without-sorting-without-map-without-tree/
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) # based on the from location
        current_trips = [] # people currently sitting in the car
        processed_trips = 0 # num of trips that have been picked up. Acts as an index to see which trip has to be picked up next since trips is now sorted based on from location
        n = len(trips)
        remaining = capacity
        time = trips[0][1] # location
        while processed_trips < n:
            # check if someone wants to get down
            # since current_trips is a heap based on to value. If the top has to value greater than time, then noone wants to get down
            while current_trips and current_trips[0][0]==time:
                # structure is [to, from, num]
                trip = heapq.heappop(current_trips)
                remaining += trip[-1]
            
            # check if someone wants to board
            while processed_trips < n and trips[processed_trips][1]==time:
                # structure is [num, from, to]
                trip = trips[processed_trips]
                if trip[0] > remaining:
                    return False
                remaining -= trip[0]
                # change structure to [to, from num]
                trip[0], trip[2] = trip[2], trip[0] 
                heapq.heappush(current_trips, trip)
                processed_trips += 1
            
            time += 1
        
        return True

