class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(num1, num2):
            if num1 == 0:
                return num2
            return gcd(num2%num1, num1)
        
        # check if they have the same structure and can be reconstructed with a 
        # common substring
        if str1+str2 != str2+str1:
            return ''
        
        n1=len(str1)
        n2=len(str2)
        divisor = gcd(n1, n2) if n1 < n2 else gcd(n2, n1)
        return str1[:divisor]


        # does not perform the initial check and explicitly check if the common
        # string divied both the input strings
        
        # def divides(str1, str2):
        #     for i in range(0, len(str2), len(str1)):
        #         if str1 != str2[i: i+len(str1)]:
        #             return False
        #     return True
        # n1=len(str1)
        # n2=len(str2)
        # divisor = gcd(n1, n2) if n1 < n2 else gcd(n2, n1)
        # common = str1[:divisor]
        # return common if divides(common, str1) and divides(common, str2) else ''
        

