class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        current = 0
        end = len(people) - 1
        result = 0
        while current <= end:
            if people[current] + people[end] <= limit:
                end -= 1
            current += 1
            result += 1
        
        return result
