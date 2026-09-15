class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            mid = s[i]
            left = i-1
            right = i+1
            r = s[i]
            count+=1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count+=1
                else: 
                    break
                left-=1
                right+=1
        for i in range(len(s)):
            left = i
            right = i+1
            r = ""
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count+=1
                else: 
                    break
                left-=1
                right+=1
        

        return count