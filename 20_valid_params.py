class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')': '(', '}': '{', ']': '['}
        for br in s:
            if br not in pairs:
                stack.append(br)
            elif len(stack)==0 or stack[-1]!=pairs[br]: #kkeping pairs dict converts 
            # the check into an or condition, which otherwise would be and condition like
            # if br=')' and stack[-1]!='(' for each bracket
                return False
            else:
                stack.pop()
        
        return len(stack)==0
                

        
