import heapq
class FreqStack:
    # priority queue
    # def __init__(self):
    #     self.stack = []
    #     self.counts = defaultdict(int)
    #     self.counter = 0
    # def push(self, val: int) -> None:
    #     self.counts[val] = self.counts[val] + 1
    #     self.counter -= 1
    #     tup = [-self.counts[val], self.counter, val]
    #     heapq.heappush(self.stack, tup)

    # def pop(self) -> int:
    #     tup = heapq.heappop(self.stack)
    #     self.counts[tup[-1]] -= 1
    #     return tup[-1]


    # O(1)
    # for each frequency we maintain a separate stack. For each element x we maintain its frequency (f) and for each stack corresponding to frequencies f' <=f we make sure that x is present in them based on the order it occurs.
    def __init__(self):
        self.counts = defaultdict(int)
        self.freq_map = defaultdict(list)
        self.max_freq = 0
    

    def push(self, val):
        self.counts[val] += 1 # update its frequency
        self.freq_map[self.counts[val]].append(val) # append to the corresponding stack
        self.max_freq = max(self.max_freq, self.counts[val]) # update the max frequency
    
    def pop(self):
        # go to stack for max frequency and pop the last element there
        result = self.freq_map[self.max_freq].pop()
        if not self.freq_map[self.max_freq]:
            self.max_freq -= 1 # update the max frequency
        
        self.counts[result] -= 1 # update the counts
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
