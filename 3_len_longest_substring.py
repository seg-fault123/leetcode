class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_length=0 
        max_length=0
        seen={}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            elif i - current_length <= seen[s[i]]:
                # essentially checks if the last seen index of the current character is
                # in the range of the current substring, basically a duplicate
                current_length = i - seen[s[i]] # update the length of the current substring by
                # sliding the window such that now it starts from the next index of the
                #previous duplicate character
                seen[s[i]] = i
            else:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                seen[s[i]] = i
        return max_length


