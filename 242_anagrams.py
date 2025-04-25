class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if length are not same then anagram is not possible
        if len(s) != len(t):
            return False
        counts=[0]*26

        ## counts all the characters in s
        for ch in s:
            counts[ord(ch)-ord('a')]+=1
        for ch in t:
            index=ord(ch)-ord('a')
            if counts[index] == 0: # if t contains a character not present in s, or
            # contains a character with more occurrences than in s
                return False
            else:
                counts[index]-=1
        ## the case where s may have a character not present in t or a chracter with more
        ## occurences than in t, is handled by checking the length at the beginning. If the 
        ## length is same, then the above situation implies that while cheking counts for
        ## characters in t, the if condition will be true and False is returned. So need for
        ## checking explicitly for the above case.
        return True

