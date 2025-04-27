class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {order[i]: i for i in range(len(order))}
        current = words[0]
        for i in range(1, len(words)):
            next_word = words[i]
            identical = True # flag if the words are identical
            for j in range(min(len(current), len(next_word))):
                if current[j] == next_word[j]:
                    continue
                elif order_index[current[j]] > order_index[next_word[j]]:
                    return False
                else:
                    identical = False
                    break
            
            if identical and (len(current) > len(next_word)):
                return False
            current=next_word
        
        return True
