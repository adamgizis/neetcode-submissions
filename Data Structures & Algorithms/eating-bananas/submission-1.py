import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        left = 1
        right = m
        lm = len(piles)
        lv = m
        while left <= right:
            mid = (left + right) // 2
            v = mid
            count = 0
            for i in piles:
                count+=math.ceil(i/v)
            if count <= h:
                lm = max(lm, count)
                lv = min(lv,v)
                right = mid -1
            else:
                left = mid + 1
        
        return lv


                


