class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # for each end point we'll maintain for what indices it conflicts with that come before it.
        left_conflicts = [[] for _ in range(n)]
        for a, b in conflictingPairs:
            a = a-1
            b = b-1
            left_conflicts[max(a, b)].append(min(a, b))
        
        # using the left_conflicts we'll calculate for each index end, if we keep that as the end point of the subarray, then what is the maximum index i before end, such that end has a conflict with i or some previous index less than end has conflict with i. Any subarray ending at end cannot start on or before i because i conflicts with some index betwene i and end. So if we calculate the subarrays possible ending at end such that no conflicts are removed then it is simply end-i (one for each starting point from [i+1,end]).
    # notice that removing any conclicts which do are lesser than i will not yield to an improvement for possible subarrays ending at end. This is because it will still include i and i has conflict with end. So best possible scenario is to remove the conflict with i.
    # If we maintain the seconf largest conflicted index encountered till now (either conflicting with end or previous indices), then that becomes the new i if i conflict is removed. So the improvement in the possibilities is that from end-i we go to end-i2, where i2 is the second largest. The improvement is exactly i-i2.
    # removal of whichever i leads to maximum improvement over all the end points, that will be added to our base answer to produce the final result
        
        base = 0 # answer when nor conflicts are removed
        bonus = defaultdict(int) # bonus[i] is the value gained by removing a conflict with i as the left.
        max_bonus = 0
        max_lefts = [-1, -1]
        for end in range(n):
            # find i and i2
            for left in left_conflicts[end]:
                if left > max_lefts[0]:
                    max_lefts = [left, max_lefts[0]]
                elif left > max_lefts[1]:
                    max_lefts[1] = left
            
            base += end - max_lefts[0]
            bonus[max_lefts[0]] +=  max_lefts[0]-max_lefts[1]
            max_bonus = max(max_bonus, bonus[max_lefts[0]])

        return base + max_bonus
