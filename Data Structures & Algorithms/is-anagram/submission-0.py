class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(0,len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 0
            else:
                s_map[s[i]] +=1
            if t[i] not in t_map:
                t_map[t[i]] = 0
            else:
                t_map[t[i]] +=1
            
        return s_map == t_map
        
