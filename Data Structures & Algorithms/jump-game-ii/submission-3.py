class Solution:
    def jump(self, nums: List[int]) -> int:
        level = 0
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add(0)
        l = len(nums)
        while queue:
            index,level = queue.popleft()
            if index == len(nums) -1:
                l = min(l, level)
            for i in range(1,nums[index]+1):
                if index + i < len(nums) and index + i not in visited:
                    queue.append((index + i,level+1))
                    visited.add(index+i)

        return l