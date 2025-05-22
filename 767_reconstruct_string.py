import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        heap = [[-val, key] for key, val in counts.items()]
        heapq.heapify(heap)
        last_char = ''
        result = ''
        while heap:
            item = heapq.heappop(heap)
            if item[1]==last_char:
                new_item = None
                if not heap:
                    return ''
                # extract the second most frequent element
                new_item = heapq.heappop(heap)
                last_char = new_item[1]
                result += new_item[1]
                new_item[0] += 1
                heapq.heappush(heap, item)
                if new_item[0] < 0:
                    heapq.heappush(heap, new_item)
            else:
                last_char = item[1]
                result+=item[1]
                item[0] += 1
                if item[0] < 0:
                    heapq.heappush(heap, item)       
        
        return result
