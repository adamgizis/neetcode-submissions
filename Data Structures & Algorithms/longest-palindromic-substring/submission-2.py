class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            mid = s[i]
            left = i-1
            right = i+1
            r = s[i]
            if len(longest) < len(r):
                    longest = r
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    r = s[left] + r + s[right]
                else: 
                    break
                if len(longest) < len(r):
                    longest = r
                left-=1
                right+=1
        for i in range(len(s)):
            left = i
            right = i+1
            r = ""
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    r = s[left] + r + s[right]
                else: 
                    break
                if len(longest) < len(r):
                    longest = r
                left-=1
                right+=1
        

        return longest
