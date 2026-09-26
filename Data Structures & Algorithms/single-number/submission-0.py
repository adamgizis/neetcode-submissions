class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     

        x_or =  0 
        for i in nums:
            x_or^=i
        
        return x_or