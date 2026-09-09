from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get the rotting friot
        def valid_fresh_oranges(pos):
            r,c = pos
            result = []
            if r+ 1 < len(grid) and grid[r+1][c] == 1:
                result.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] == 1:
                result.append((r-1,c))
            if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                result.append((r,c+1))
            if c-  1 >= 0 and grid[r][c-1] == 1:
                result.append((r,c-1))
            return result



        queue = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    count+=1
        nq = deque()
        visited = set()
        minutes = 0
        while queue:
            pos = queue.popleft()

            for p in valid_fresh_oranges(pos):
                if p not in visited:
                    nq.append(p)
                    visited.add(p)

            if (not queue) and nq:
                queue = nq
                nq = deque()
                minutes+=1

        return minutes if len(visited) == count else -1

            
            
                