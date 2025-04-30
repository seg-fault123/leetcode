class Solution:
    ## for each string in the list, the key can be either the sorted string of characters (all anagrams will have the same sorted string of characters) or the count tuple of the characters in the string.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for element in strs:
            sorted_element = ''.join(sorted(element))
            if sorted_element in groups:
                groups[sorted_element].append(element)
            else:
                groups[sorted_element]=[element]
            # counts = [0]*26
            # for char in element:
            #     counts[ord(char)-ord('a')]+=1
            # counts = tuple(counts)
            # if counts in groups:
            #     groups[counts].append(element)
            # else:
            #     groups[counts] = [element]
        
        
        return list(groups.values())
