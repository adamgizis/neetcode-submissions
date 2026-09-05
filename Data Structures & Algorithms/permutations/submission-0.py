class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        indices = set()
        nums_len = len(nums)
        def dfs(index):
            if len(current) == nums_len:
                res.append(current.copy())
                return
            for i in range(0, len(nums)):
                if i in indices:
                    continue
                indices.add(i)
                current.append(nums[i])
                dfs(i)
                current.pop()
                indices.remove(i)

            
            return
        dfs(-1)

        return res