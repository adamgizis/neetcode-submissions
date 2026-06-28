from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = Counter()
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1map[s1[i]]+=1
    
        s2map = Counter()
        for i in range(len(s1)):
            s2map[s2[i]]+=1

        left = 0
        right = len(s1)
        if s1map == s2map:
            return True
        while right < len(s2):
            s2map[s2[left]]-=1
            s2map[s2[right]]+=1
            if s1map == s2map:
                return True
            left +=1
            right+=1
        
        return s1map == s2map
            

            

    