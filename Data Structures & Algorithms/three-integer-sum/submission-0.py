class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        p = set()
        n = sorted(nums)
        print(n)
        print(n)
        for i in range(len(n)):
            target = n[i]
            left = i + 1
            right = len(n) -1
            while left < right:
                s = n[left] + n[right]
                if s == -target:
                    t = sorted([n[left], target, n[right]])
                    if tuple(t) not in p:
                        p.add(tuple(t))
                        result.append(t)
                if s > -target:
                    right-=1
                else:
                    left+=1

        return result

