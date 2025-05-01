class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_speed(k):
            remaining = h
            n = len(piles)
            for i in range(n):
                if piles[i]%k == 0 :
                    remaining -= piles[i]//k
                else:
                    remaining -= piles[i]//k + 1
            
            return remaining >= 0
        
        start = 1
        end = piles[0]
        for i in range(1, len(piles)):
            end = max(end, piles[i])
        
        ans = end
        while start <= end:
            mid = (start+end)//2
            if valid_speed(mid):
                ans = mid
                end = mid -1
            else:
                start = mid + 1
        
        return ans
