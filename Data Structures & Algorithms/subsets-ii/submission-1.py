class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        cur = []
        def dfs(index, mlength):
            print(cur)
            result.append(cur.copy())
            if len(cur) == mlength:
                return
            prev = -21
            for i in range(index+1, len(nums)):
                if nums[i] != prev:
                    cur.append(nums[i])
                    dfs(i, mlength)
                    cur.pop()
                prev = nums[i]

            return

        count = 0
        prev = -21
        dfs(-1,0)
        while count < len(nums):
            if nums[count] != prev:
                cur = [nums[count]]
                dfs(count, len(nums) - count)
            prev = nums[count]
            count+=1
        
        return result
            

            
    


