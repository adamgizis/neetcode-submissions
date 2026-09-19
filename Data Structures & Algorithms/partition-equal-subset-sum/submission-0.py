class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        results = set()
        total_sum = sum(nums)
        curSum = 0
        n = set()
        def dfs(index):
            nonlocal curSum
            if curSum == sum(nums) - curSum:
                return True
            for i in range(index + 1, len(nums)):
                if curSum + nums[i] <= sum(nums) - curSum and curSum + nums[i] not in n:
                    curSum+=nums[i]
                    n.add(curSum)
                    if dfs(i):
                        return True
                    curSum-=nums[i]
            
            return False
        for i in range(-1, len(nums)):
            if dfs(i):
                return True
        
        return False