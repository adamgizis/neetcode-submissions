class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash map difference and index
        diffs = {}




        for i,n in enumerate(nums):
            print(i,n)
            if (target - n) in diffs:
                return [diffs[target-n], i]
            print(target-n)
            diffs[n] = i
        
        return [0,0]

        