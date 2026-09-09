from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))

        visited = set(queue.copy())
        def valid_neighbors(pos):
            r,c = pos
            result = []
            if r+ 1 < len(grid) and grid[r+1][c] != -1:
                result.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] != -1:
                result.append((r-1,c))
            if c + 1 < len(grid[0]) and grid[r][c+1] != -1:
                result.append((r,c+1))
            if c-  1 >= 0 and grid[r][c-1] != -1:
                result.append((r,c-1))

            return result
        while queue:
            print("here")
            pos = queue.popleft()
            neighbors = valid_neighbors(pos)
            if grid[pos[0]][pos[1]] != 0:

                m = grid[pos[0]][pos[1]]
                for p in neighbors:
                    m = min(grid[p[0]][p[1]], m) 
                grid[pos[0]][pos[1]] = m + 1
            
            for n in valid_neighbors(pos):
                if n not in visited:
                    visited.add(n)

                    queue.append(n)

            