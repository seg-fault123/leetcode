from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        visited = {word: False for word in wordList}
        if endWord not in visited:
            return 0

        def neighbor_words(word, replace_index, ignore):
            # generate new words by replacing at the replace_index position and not generating word which has "ignore" at replace index position 
            for char in chars:
                if char!=ignore:
                    new_word = word[:replace_index] + char + word[replace_index+1:]
                    yield new_word
        
        q = deque()
        visited[beginWord] = True
        level = 1
        q.append((beginWord, level))
        while q:
            word, level = q.popleft()
            # generate new words by replacing chars at each index
            for index in range(len(word)):
                for neighbor in neighbor_words(word, index, word[index]):
                    if neighbor==endWord:
                        return level+1
                    elif neighbor in visited and not visited[neighbor]:
                        q.append((neighbor, level+1))
                        visited[neighbor] = True
        
        # endWord cannot be achieved
        return 0



# more optimized solution, created masks
# class Solution:
#     masks = {}
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:    
#         # generate a mask to word map
#         word_set = set(wordList)
#         word_set.add(beginWord)
#         mask_to_words = defaultdict(list)
#         for word in word_set:
#             for i in range(len(beginWord)):
#                 mask = word[:i] + "*" + word[i+1:]
#                 mask_to_words[mask].append(word)

#         queue = deque([(beginWord, 1)])
#         visited = set()
#         while queue:
#             word, depth = queue.popleft()
#             if word == endWord:
#                 return depth
#             for i in range(len(beginWord)):
#                 current_mask = word[:i] + "*" + word[i+1:]
#                 for neighbor_word in mask_to_words[current_mask]:
#                     if neighbor_word not in visited:
#                         visited.add(neighbor_word)
#                         queue.append((neighbor_word, depth + 1))
#         return 0




