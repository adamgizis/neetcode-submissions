class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {} # maps number to index

        for i, val in enumerate(nums):
            if target - val in pos:
                return [pos[target-val], i]
            pos[val] = i
        
        return []