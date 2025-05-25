import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize != 0:
            return False

        counts = {}
        for num in hand:
            counts[num] = counts.get(num, 0) + 1
        heap = [[key, val] for key, val in counts.items()]
        heapq.heapify(heap)
        while heap:
            temp = [] # to track the current group
            for i in range(groupSize):
                if not heap:
                    return False
                item = heapq.heappop(heap)
                # if the current element is not consecutive 
                if i > 0 and (temp[i-1][0]+1) != item[0]:
                    return False
                item[1] -= 1
                temp.append(item)
            for item in temp:
                if item[1]>0:
                    heapq.heappush(heap, item)
        
        return True
            
            
                    
        
