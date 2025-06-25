class Solution:
    def checkValidString(self, s: str) -> bool:
        open_max = 0
        open_min = 0
        # track the maximum and minimum possible open brackets at any step
        
        for char in s:
            if char=='(':
                # add to both
                open_max += 1
                open_min += 1
            elif char==')':
                # decrement both
                open_max -= 1
                open_min -= 1
            else:
                # char is *, it can act as (, update max, it can also act as )
                # decrement min
                open_max += 1
                open_min -= 1

            if open_max < 0:
                # it means even after considering all * as (, still there are not enough ( to match with ).
                return False

            # we have unneccessarily made * as ), revert to balanced state
            open_min = max(open_min, 0)

        return open_min==0 
                        
