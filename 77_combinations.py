class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def make_combination(number, num_included, current):
            if num_included==k:
                return [current]
            if number>n:
                return []
            
            temp = make_combination(number+1, num_included, current)
            temp += make_combination(number+1, num_included+1, current+[number])
            return temp
        
        return make_combination(1, 0, [])
