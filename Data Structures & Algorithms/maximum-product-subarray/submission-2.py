class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_nums = 1
        min_nums = 1
        res = nums[0]

        for val in nums:
            l = [max_nums * val, min_nums*val, val]
            max_nums = max(l)
            min_nums = min(l)
            res = max(max_nums,res)


        return max(max_nums,res)



            