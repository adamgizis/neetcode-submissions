from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1,7,10 -> 14
        # 7,7 -> 14
        #10,1,1,1,1

        queue = deque()
        mcount  = 10001
        queue.append((0,0))
        visited = {0}
        while queue:
            value,count = queue.popleft()
            if value == amount:
                mcount = min(count, mcount)
                continue
            if value < amount:
                for i in coins:
                    if value + i <= amount and value + i not in visited:
                        queue.append((value + i, count+1))
                        visited.add(value + i)

        if mcount == 10001:
            return -1
        
        return mcount

