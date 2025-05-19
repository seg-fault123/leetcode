class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a car can only be slowed down by the cars in front of it
        # sort the cars based on their position and based on their sorted order,
        # calculate the required time to reach target by each car
        # the car closest to target cannot be slowed down and reaches target at its
        # calculated time.
        # If we iterate back to previous cars, and if the current car is anticipated 
        # to reach before the cars in front, it will slow down and form a fleet with the cars in front.
        # Otherwise it forms a fleet of its own and maybe with the cars behing it, that may catch up to it.
        # To see if the current car can catch up to its cars in front we maintain a
        # max_time variable, if the current car can reach before max_time, it will catch up to the cars in front. If the current car needs more time than max_time then
        # it forms its own fleet
        
        n = len(position)
        times = [(position[i], (target-position[i])/speed[i]) for i in range(n)]
        times.sort()
        fleets = 0
        max_time = 0
        for i in range(n-1, -1, -1):
            if times[i][1] > max_time:
                fleets+=1
                max_time = times[i][1]
        
        return fleets
