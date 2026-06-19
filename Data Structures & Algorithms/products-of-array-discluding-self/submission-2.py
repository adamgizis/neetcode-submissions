class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        pre_zeros = 1

        zero_count = 0
        for i in nums:
            product*= i
            if i != 0:
                pre_zeros*=i
            else:
                zero_count +=1
        result = []
        for i in nums:
            if zero_count > 1:
                result.append(0)
            else:
                temp = 0
                if i!= 0:
                    temp = product/i
                else:
                    temp = pre_zeros
                result.append(int(temp))

        return result
        