class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_0 = False
        found_1 = False
        found_2 = False

        # check if the current triplet exceeds target in any dimension. If so, it cannot be merged with any triplet as it will produce a result which will exceed target in that dimension. If it doesnt exceed in any dimension then check if it equals target in some dimension. Now merging with other triplets will possibly bring it closer to target 
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
            
            found_0 |= triplet[0]==target[0]
            found_1 |= triplet[1]==target[1]
            found_2 |= triplet[2]==target[2]
        
        return found_0 and found_1 and found_2

