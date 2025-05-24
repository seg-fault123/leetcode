class Solution:
    def numDecodings(self, s: str) -> int:
        result = [None]*len(s)
        # result[i] specifies the number of decodings for s[i:]
        def count_decodings(index):
            if index==len(s):
                return 1
            elif result[index] is not None:
                return result[index]
            elif s[index]=='0':
                # starting character is '0', so 0 decodings possible
                result[index]=0
                return 0
            
            # decode the current character as it is
            temp = count_decodings(index+1)
            if index < len(s)-1:
                # merge two characters (current and next)
                if int(s[index:index+2])<=26:
                    temp += count_decodings(index+2)
            result[index]=temp
            return temp
        return count_decodings(0)

