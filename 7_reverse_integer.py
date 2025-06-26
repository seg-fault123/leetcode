class Solution:
    def reverse(self, x: int) -> int:
        # check if x==-2**31, this value is -2147483648, whose reverse is out of bounds. Moreover since we convert negative to positive temporarily in our code, we can't convert -2**31 to positive since it is out of bounds itself
        if x == -(2**30) - (2**30):
            return 0

        # will be used later
        max_val = (2**30 + (2**30-1))//10
        negative = False
        if x < 0:
            negative = True
            x = -x
        result = 0
        while x!=0:
            digit = x%10 # extract the digit
            # check if adding this digit to our result will be out of bounds
            if result > max_val or (result==max_val and digit>7):
                return 0
            
            result = result*10 + digit
            x //= 10
        
        if negative:
            result = -result
        
        return result
        

