class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb_sum(index, target, current=[]):
            if target == 0:
                return [current]
            elif (target <= 1) or (index == len(candidates)):
                return []
            
            temp = comb_sum(index, target - candidates[index], current + [candidates[index]]) # include the current number and check if can be included again

            temp += comb_sum(index+1, target, current) # don't include this number

            return temp
        
        return comb_sum(0, target)


