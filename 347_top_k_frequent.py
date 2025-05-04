class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        frequencies = [[] for _ in range(len(nums)+1)]
        for key, value in counts.items():
            frequencies[value].append(key)
        result = []
        for i in range(len(frequencies)-1, -1, -1):
            if len(result) == k:
                return result
            else:
                result.extend(frequencies[i])

