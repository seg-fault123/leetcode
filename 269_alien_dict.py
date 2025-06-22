class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {}
        # first make an adj_list such that if some char1 < char2 then char1 should transitively occur in some list
        # starting from adj_list[char2]
        def make_dependency_graph(start, end, index):
            # start and end both are included
            if start==end:
                # only single word is there no information can be extracted
                # just add empty list for chars not seen yet
                for char in words[start]:
                    if char not in adj_list:
                        adj_list[char] = []
                return
            
            # if they are truly lexi sorted then for each word from start till end
            # the chars match till index-1. If index is out of bouds then all exhausted strings should
            # present in the list at the front itself. No need to check these strings skip them by updating the start

            # check if indices are exhausted
            while len(words[start])==index and start<end:
                start += 1
            
            # at max start will be equal to end or a word is found which is not yet exhausted
            # start checking from next word
            current = start+1
            while current<=end:
                # if they are same till index as well then make their group update the current pointer
                if words[current][index] == words[start][index]:
                    current += 1
                else:
                    break
            # either current is end+1 and points to a word that differs at index position
            # in both cases look for order at index+1 in the group which is equal at index 
            make_dependency_graph(start, current-1, index+1)

            # a word is found where current differs at index
            if current <= end:
                current_char = words[current][index]
                start_char = words[start][index]
                # update the adj_list
                if current_char in adj_list:
                    adj_list[current_char].append(start_char)
                else:
                    adj_list[current_char] = [start_char]

                # look for order starting at current at the same index level
                make_dependency_graph(current, end, index)
            
            return
        
        # if they are not sorted lexi, then index error may occur
        try:
            make_dependency_graph(0, len(words)-1, 0)
        except IndexError:
            return ''

        result = ['']
        visited = {char: 0 for char in adj_list}

        def dfs(char):
            if visited[char]==2:
                return True
            
            visited[char] = 1
            for before in adj_list[char]:
                # cycle is detected
                if visited[before]==1 or not dfs(before):
                    return False
            # add to result
            result[0] += char
            visited[char] = 2
            return True
        
        for char in adj_list:
            if visited[char]==0 and not dfs(char):
                return ''
        
        return result[0]
