from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # ban the next senator of the opposition party
        r_q = deque()
        d_q = deque()
        next_index = 0
        for senator in senate:
            if senator=='R':
                r_q.append(next_index)
            else:
                d_q.append(next_index)
            next_index += 1
        
        while len(r_q) and len(d_q):
            r_i = r_q.popleft()
            d_i = d_q.popleft()

            if r_i < d_i:
                # radiant guy gets a vote before dire guy
                # ban the dire guy from next round by reinserting the radiant guy in its queue with the updated voting number
                r_q.append(next_index)
            else:
                # reverse of the above case
                d_q.append(next_index)
            next_index += 1
        
        if len(r_q):
            return 'Radiant'
        else:
            return 'Dire'
        
