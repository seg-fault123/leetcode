class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb_sum(index, target, current, seen):
            if target == 0:
                return [current]
            if index==len(candidates) or target<0:
                return []
            
            temp = []
            number = candidates[index]
            if number not in seen:
                temp = comb_sum(index+1, target-number, current+[number], seen)
            temp += comb_sum(index+1, target, current, seen.union([number]))
            return temp
        
        return comb_sum(0, target, [], set())
