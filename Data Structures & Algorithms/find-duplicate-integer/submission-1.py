class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slowp = 0
        fastp = 0
        while True:
            if slowp == fastp and slowp != 0:
                break

            slowp = nums[slowp]
            fastp = nums[nums[fastp]]

        # the second point is the cycle entry
        slow2 = 0
        while True:
            slowp = nums[slowp]
            slow2 = nums[slow2]
            if slowp == slow2:
                return slowp

        
