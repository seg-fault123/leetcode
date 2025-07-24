class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4 != 0 or len(matchsticks)<4:
            return False
        
        target = total / 4
        sides = [0, 0, 0, 0]
        memo = {}
        matchsticks.sort(reverse= True)
        def make_square(index, target):
            if index==len(matchsticks):
                return True
            # make a configuration, configuration (side lenght 1,2,3,5) is same as (side length 3,2,1,5) only the sides are jumbled. If we have already calculated a similar configuration, return the stored result in the memo

            # to map similar configurations to the same value, sort the side lenghts
            key = f'{index}' + ',' + ','.join([str(x) for x in sorted(sides)])
            if key in memo:
                return memo[key]
            
            for i in range(4):
                side = sides[i]+matchsticks[index]
                if side <= target:
                    sides[i] = side
                    if make_square(index+1, target):
                        memo[key] = True
                        return True
                    sides[i] -= matchsticks[index]
            memo[key] = False
            return False
        
        return make_square(0, target)
