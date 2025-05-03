class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a)-1
        j = len(b)-1
        result = ''
        
        while i>=0 or j>=0 or carry>0:
            if i>=0:
                carry += int(a[i])
                i -= 1
            if j >=0:
                carry += int(b[j])
                j -= 1
            
            result = str(carry%2) + result
            carry //= 2
        return result
        
        
                

                


