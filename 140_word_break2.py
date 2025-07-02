class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        word_set = set(wordDict)

        # returns all the sentences formed with s[index:]
        def make_words(index, s):
            # if index==len(s):
            #     # base case is reached, valid sentence is formed
            #     return ['']
            if index in memo:
                return memo[index]
            
            # try to form words starting at s[i]
            for end in range(index+1, len(s)+1):
                if s[index:end] in word_set:
                    # a valid word is found
                    result = [] # list of sentences that have this valid word as the starting word
                    if end == len(s):
                        # if no more characters are left, then just append this word to the result
                        result.append(s[index:end])
                    else:
                        # more characters are left
                        # extract the sentences starting at end 
                        for sentence in make_words(end, s):
                            # add this word to the starting of the sentence with space in between
                            result.append(s[index:end]+' '+sentence)
                    
                    # add to the memo
                    if index in memo:
                        memo[index] += result
                    else:
                        memo[index] = result
            
            # if no word matched from index then set the result as empty list as no sentences were formed
            if index not in memo:
                memo[index] = []
            
            return memo[index]
        
        return make_words(0, s)

