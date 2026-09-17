class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_num = 1
        min_num = 1
        res = nums[0]

        for val in nums:
            l = [max_num * val, min_num * val, val]
            # val
            max_num = max(l)
            min_num = min(l)
            res = max(res, max_num)




        return res



            