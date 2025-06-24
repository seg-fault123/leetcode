class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        curr = 0
        cum_total = []
        for num in piles:
            curr += num
            cum_total.append(curr)
        
        def optimal(start, m):
            if start==len(piles):
                return 0
            elif (start, m) in memo:
                return memo[(start, m)]
            
            total = None
            if start==0:
                total = cum_total[-1]
            else:
                total = cum_total[-1] - cum_total[start-1]
            
            result = 0
            for i in range(1, 2*m+1):
                new_start = start+i
                if new_start > len(piles):
                    break
                result = max(result, total-optimal(new_start, max(i, m)))
            
            memo[(start, m)] = result
            return result
        
        result = optimal(0, 1)
        # print(memo)
        return result


        
