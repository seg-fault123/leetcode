class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for element in strs:
            result.append(str(len(element))+','+element)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        current = 0
        while current < len(s):
            if s[current]==',':
                length = int(s[start:current])
                result.append(s[current+1 : current+length+1]) 
                current = current+length+1
                start = current
            else:
                current += 1
        
        return result

