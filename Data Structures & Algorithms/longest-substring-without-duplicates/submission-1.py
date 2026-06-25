class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        p = set()
        largest = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in p:
                p.add(s[right])
            else:
                # get to the inital instance of this thing
                while s[right] in p:
                    p.remove(s[left])
                    left+=1
                p.add(s[right])
            largest = max(largest, right- left + 1)
            
        return largest
            
            
                