class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi',
                    '5': 'jkl', '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
        
        result = []
        def make_combination(index, current=''):
            if index == len(digits):
                result.append(current)
                return
            
            for char in mapping[digits[index]]:
                make_combination(index+1, current+char)

                
        if digits!='':
            make_combination(0, '')
        return result
