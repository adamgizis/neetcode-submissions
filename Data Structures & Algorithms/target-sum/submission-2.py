class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        val = {}
        def dfs(i,a):
            if i >= len(nums) and a == target:
                return 1
            if i >= len(nums) and a != target:
                return 0 
            res = 0
            if (i+1, a + nums[i]) in val:
                res = val[(i+1, a + nums[i])]
            else:
                res = dfs(i+1, a + nums[i])
            if (i+1, a - nums[i]) in val:
                res += val[(i+1, a - nums[i])]
            else:
                res += dfs(i+1, a - nums[i])
            val[(i,a)] = res
            return res

        return dfs(0,0)