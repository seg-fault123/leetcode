class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
    # let top score be the score which is greater and let top_strig be the corresponding string

    # in first part we try to remove all possible top strings from the input string
    # suppose ab is the top string
    # when we remove all possible ab from the input string, it is impossible to get ab back after we remove ba from the trimmed string. 
    # we always make the greedy choice because it leads to optimal result
        top_score = x
        top_string = 'ab'

        bottom_score = y
        bottom_string = 'ba'

        if y > x:
            top_score, bottom_score = bottom_score, top_score
            top_string, bottom_string = bottom_string, top_string
        
        stack = []
        score = 0
        # remove the top_string
        for char in s:
            if stack and stack[-1]+char == top_string:
                score += top_score
                stack.pop()
            else:
                stack.append(char)
        
        # remove the bottom string
        stack2 = []
        for char in stack:
            if stack2 and stack2[-1]+char == bottom_string:
                score += bottom_score
                stack2.pop()
            else:
                stack2.append(char)
        
        return score
