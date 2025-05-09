import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort(key= lambda x: x[0])
        current_time = tasks[0][0]
        index = 0
        result = []
        heap = []
        while index < n or heap:
            # add all the tasks that can be performed
            while index < n and tasks[index][0] <= current_time:
                heapq.heappush(heap, tasks[index][1:])
                index += 1
            if heap:
                # perfrom the appropriate task
                task = heapq.heappop(heap)
                result.append(task[-1])
                current_time += task[0]
            else:
                # cpu is idle, update the current time
                current_time = tasks[index][0]
        
        return result
