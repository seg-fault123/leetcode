class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # simulate multiplication by hand

        # this functions takes a string number and multiplies with a single digit
        def mul(num1, single_num):
            if single_num==0:
                return 0
            
            carry = 0
            index = len(num1)-1
            base = 1
            result = 0
            while index>=0 or carry>0:
                temp = 0
                if index >= 0:
                    temp += int(num1[index])

                temp = temp*single_num + carry
                carry = temp//10
                result += (temp%10)*base
                index-=1
                base *= 10
            
            return result


        if num1=='0':
            return '0'
        elif num2=='0':
            return '0'
        
        result = 0
        base = 1
        index = len(num2)-1
        # take digits of num2 and multiply with num1
        while index>=0:
            temp = mul(num1, int(num2[index]))
            result += base*temp
            base *= 10
            index -= 1
        
        return str(result)
        
