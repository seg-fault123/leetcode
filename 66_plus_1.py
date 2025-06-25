class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        stack = []
        curr = len(digits)-1
        while curr>=0 or carry>0:
            result = carry
            if curr>=0:
                result += digits[curr]
            
            carry = result//10
            stack.append(result%10)
            curr -= 1
        
        return stack[::-1]
