class Solution:
    # well maintain a max possible window. The window is created such that:
    # 1) it contains a character with maximum counts in the window and
    # some other k characters which can be flipped
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_count = 0
        # each iteration tries to increase the size of the window by 1
        # at the end, the size of the window gives us the answer
        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1
            max_count = max(max_count, counts[s[right]])

            # the window contains more flipped characters than k, then
            # reduce the window size to previous size
            if right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1
            
        return len(s) - left
