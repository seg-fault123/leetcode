class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0, 0, 0, 0]
        def make_square(index, target):
            if index==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]
            
            for i in range(4):
                # check if current side already exceeds the target side
                if sides[i]+matchsticks[index] > target:
                    continue
                sides[i] += matchsticks[index]
                if make_square(index+1, target):
                    return True
                sides[i] -= matchsticks[index]
            
            return False

        total = sum(matchsticks)
        # check if 4 equal sides are possible
        if total%4 != 0:
            return False
        matchsticks.sort(reverse=True)
        target = total//4
        return make_square(0, target)
