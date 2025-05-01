import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the first value is the waiting period required before we can do that task
        # the second value is the negative of frequncy of the tasks left. The most
        # frequent task is given the most prirority in the min heap.
        # idle has [0, 1] (only one with a positive frequency)

        heap = [[0, 0] for _ in range(27)]
        for task in tasks:
            heap[ord(task) - ord('A')][1] -= 1
        heap[26][1] = 1 # idle
        intervals = 0
        heapq.heapify(heap)

        while len(heap) > 1:
            element = heapq.heappop(heap)
            if element[1] == 0: # if zero is encounterd, ignore, will only occur
            # when the initial zero alphabets are there
                continue

            elif element[1] == 1:
                # if idle is encountered
                intervals+=1

            else:
                # if task is encountered
                intervals+=1
                element[0] = n # update the required timesteps
                element[1] += 1 # update the frequency count

            for i in range(len(heap)):
                # update the required timestep of other taks
                if heap[i][0]==0:
                    continue
                heap[i][0] -= 1

            if element[1]==1 or element[1]<0:
                # push only if idle or frequency is not zero
                heapq.heappush(heap, element)
            heapq.heapify(heap)
            
        return intervals
