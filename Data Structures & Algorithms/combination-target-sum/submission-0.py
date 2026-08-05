class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        #i equals the index
        cur = []
        def dfs(i):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target:
                return
            for index in range(i,len(nums)):
                cur.append(nums[index])
                dfs(index)
                cur.pop()
            return
        
        dfs(0)
        return res