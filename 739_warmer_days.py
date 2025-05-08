class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0]*len(temperatures)
        stack = []
        # if you find a warmer day, update the answers for previous days
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answers[prev_index] = i - prev_index
            stack.append(i)
        
        return answers



        # we start with the last day and base case is 0 for last index.
        # if the current day is colder then just return the day we are checking
        # if the current day is warmer, go to the index/day which is warmer than the 
        # index/day we were comparing current day with. Already calculated in answers
        # as we were coming in reverse order

        # def correct_index(index, current_index):
        #     if index==len(temperatures):
        #         return current_index
        #     elif temperatures[current_index] >= temperatures[index]:
        #         next_index = index + answers[index]
        #         if next_index == index:
        #             return current_index
        #         else:
        #             return correct_index(next_index, current_index)
        #     else:
        #         return index
        # for i in range(len(temperatures)-1, -1, -1):
        #     answers[i] = correct_index(i+1, i) - i
        # return answers
