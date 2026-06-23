class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        m = left

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mi = (mid + m) % len(nums)

            if nums[mi] == target:
                return mi
            
            if nums[mi] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
