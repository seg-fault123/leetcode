class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total =0

        for i in range(n):
            total += gas[i] - cost[i]
        
        # if sum of surplus gas is negative, we can't make the circle
        if total <0 :
            return -1
        
        # if the cummulative falls below zero, move to the next index to start as we
        # cannot complete the round starting from any index in the range [previous start, current i]
        current_tank = 0
        start = 0
        for i in range(n):
            current_tank += gas[i]-cost[i]
            if current_tank < 0:
                current_tank = 0
                start = i+1
        
        return start
