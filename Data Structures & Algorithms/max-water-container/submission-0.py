class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mArea = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            mArea = max(mArea, height * width )
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
            
        return mArea