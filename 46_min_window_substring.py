class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # maintain a window
        start = 0
        min_window = [0, len(s)]
        char_count = defaultdict(int) # to keep track of what characters are required and by how much
        for char in t:
            char_count[char] += 1

        remaining = len(t) # to keep track of how many more characters are required to match in s

        for end, char in enumerate(s):

            if char_count[char] > 0:
                # this means that this character is required
                remaining -= 1
            # for unnecessary chars, char_count will be negative
            char_count[char] -= 1
        
            if remaining==0:
                # all chars are matched, try to shrink the window
                while char_count[s[start]] < 0:
                    # this means that char at starting is unneccessary and window can shrink
                    char_count[s[start]] += 1
                    start += 1
                
                # the start character now is required and window is shrunk as much possible

                if min_window[1]-min_window[0] > end - start:
                    # update the min window
                    min_window[0], min_window[1] = start, end
                
                # slide the window as this window is valid and we want to find smaller windows, but if we keep the start the same, then the window size will only increase. So slide to next window and see if smaller windows can be found
                char_count[s[start]] += 1
                remaining += 1
                start += 1

        return "" if min_window[1]==len(s) else s[min_window[0] : min_window[1]+1]

