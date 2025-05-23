class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def mutations(current):
            for i in range(4):
                temp = current[:i] + str((int(current[i])+1)%10) + current[i+1:]
                yield temp
                temp = current[:i] + str((int(current[i])-1)%10) + current[i+1:]
                yield temp

        visited = set(['0000'])
        deadends = set(deadends)

        if '0000' in deadends:
            # can't move forward
            return -1
        
        q = ['0000']
        moves = 0
        # if a node is in q, it has already been added to visited, this makes sure
        # that we do not add the same node twice in the q
        while q:
            temp = []
            for current in q:
                if current==target:
                    return moves
                for new_node in mutations(current):
                    if new_node not in deadends and new_node not in visited:
                        visited.add(new_node)
                        temp.append(new_node)
            q = temp
            moves += 1
        
        return -1
        
        
            




