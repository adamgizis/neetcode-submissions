class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = nums[0]
        for index, val in enumerate(nums):
            if count < 0:
                return False
            count = max(count, nums[index])
            count-=1

        return True