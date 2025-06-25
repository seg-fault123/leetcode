class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        indices = {}
        # maintain the last of occurrence of each char
        for i, char in enumerate(s):
            indices[char] = i
        
        start = 0
        while start < len(s):
            # find the last place which has to be included in this interval
            end = indices[s[start]]
            current = start+1
            # for all the characters in between this interval, keep updating the end pointer as all of them now have to be included in this same interval
            while current <= end:
                if indices[s[current]] > end:
                    end = indices[s[current]]
                current += 1
            # we have found the end of this interval, update the start of the next interval
            result.append(current-start)
            start = current
        
        return result
