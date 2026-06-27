from collections import deque
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        mmap = Counter()
        gmax = 0
        for right in range(len(s)):
            # check if the new window is valid
            mmap[s[right]]+=1
            while (right - left + 1) - max(mmap.values()) > k:
                mmap[s[left]]-=1
                left +=1
            gmax = max(gmax, right - left + 1)

        return gmax
            
