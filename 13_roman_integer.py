class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        
        # check string in reverse, if the current char has a greater value than the char that was processed earlier, then just add to result
        # othervise subtract the current char value from the result
        prev_val = 0
        result = 0
        for char in s[::-1]:
            if val[char] < prev_val:
                result-=val[char]
            else:
                result+= val[char]
            prev_val = val[char]
        return result
