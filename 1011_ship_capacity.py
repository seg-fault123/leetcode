class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(capacity):
            days_required = 1
            cum_sum = 0
            for i in range(len(weights)):
                if cum_sum + weights[i] > capacity:
                    cum_sum = weights[i]
                    days_required += 1
                else:
                    cum_sum += weights[i]
            
            return days_required <= days

        start = weights[0]
        end = weights[0]
        for i in range(1, len(weights)):
            start = max(start, weights[i])
            end += weights[i]
        
        ans = end
        while start <= end:
            mid = (start + end)//2
            if is_valid(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid+1
        
        return ans
