class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        total = nums[0]
        for i,val in enumerate(nums):
            if i == 0:
                continue
            cur = max(cur + val, val)
            total = max(total,cur)

        return total
