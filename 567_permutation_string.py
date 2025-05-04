class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counts = {}
        s2_counts = {}
        for i in range(len(s1)):
            s1_counts[s1[i]] = 1 + s1_counts.get(s1[i], 0)
            s2_counts[s2[i]] = 1 + s2_counts.get(s2[i], 0)
        
        if s1_counts == s2_counts:
            return True
        
        remove = 0
        for include in range(len(s1), len(s2)):
            s2_counts[s2[include]] = 1+ s2_counts.get(s2[include], 0)
            s2_counts[s2[remove]] -= 1
            if s2_counts[s2[remove]] == 0:
                del s2_counts[s2[remove]]
            
            if s2_counts == s1_counts:
                return True

            remove += 1
        
        return False
