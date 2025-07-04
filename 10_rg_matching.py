class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        # returns true or false is s[i:] matches p[j:]
        def parse(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            elif i>=len(s) and j>=len(p):
                # both have been exhausted, successful match
                return True
            elif j>=len(p):
                # s still left but pattern exhausted, return false
                return False
            
            # see if current characters match
            char_match = i<len(s) and (s[i]==p[j] or p[j]=='.')

            # see if next char is a star
            if j+1 < len(p) and p[j+1]=='*':
                # we have two possibilities, to use the star in case of match, or ignore it
                result = (char_match and parse(i+1, j) or parse(i, j+2))
                memo[(i, j)] = result
                return result
            else:
                # check if current matches and next also matches
                result = char_match and parse(i+1, j+1)
                memo[(i, j)] = result
                return result
        
        return parse(0, 0)
