class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable = [False]*len(s)
        reachable[0] = True # is index reachable from index 0
        count = 0 # number of indices in the window [i-maxjump, i-minjump] that allow jumping to current
        for i in range(1, len(s)):
            if i > maxJump:
                count -= int(reachable[i-maxJump-1]) # this index is out of bounds and does not jump to current index
            if i >= minJump:
                count+= int(reachable[i-minJump]) # this index is now in range of the window
            if count>0 and s[i]=='0': 
                # if some index in the window can jump to the current index
                reachable[i] = True        
        # fo the index range (0, minJump), open interval, the count remains 0. For index [minJump, maxJump], it remains atleast 1 because one can jump from 0th index. At maxJump + 1, 1 is subtracted from the count because 0 can no longer reach there. This is done for all indices

        return reachable[len(s)-1]
