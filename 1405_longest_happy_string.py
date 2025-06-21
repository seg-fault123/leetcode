import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # to maintain how many times the character came consecutively
        occurrence = {'a': 0, 'b': 0, 'c': 0}
        heap = [[-val, char] for val, char in [[a, 'a'], [b, 'b'], [c, 'c']] if val>0]
        heapq.heapify(heap)
        result = ''
        while heap:
            item = heapq.heappop(heap)
            # check if char is valid or not
            if occurrence[item[1]]==2:
                # no more characters available
                if not heap:
                    return result
                # if characters available then use those chars
                new_item = heapq.heappop(heap)
                result += new_item[1]
                new_item[0] += 1
                occurrence[new_item[1]] += 1

                heapq.heappush(heap, item)
                # update occurrence of other chars
                for char in occurrence:
                    if char!=new_item[1]:
                        occurrence[char]=0
                if new_item[0] < 0:
                    heapq.heappush(heap, new_item)
            else:
                result += item[1]
                occurrence[item[1]] += 1
                item[0] += 1
                #update occurrence of other chars
                for char in occurrence:
                    if char!=item[1]:
                        occurrence[char]=0
                if item[0] < 0:
                    heapq.heappush(heap, item)
        
        return result


