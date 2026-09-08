class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        stack = []
        num_islands = 0
        

        def valid_moves(pos):
            r,c = pos
            result = []
            if r + 1 < len(grid):
                result.append((r+1, c))
            if r-1 >= 0:
                result.append((r-1,c))
            if c + 1 < len(grid[0]):
                result.append((r,c+1))
            if c-1 >= 0:
                result.append((r,c-1))
            return result

        area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    num_islands = max(area, num_islands)
                    area = 0
                    visited.add((i,j))
                    stack = [(i,j)]
                    while stack != []:
                        area +=1
                        r,c = stack.pop()
                        for pos in valid_moves((r,c)):
                            x,y = pos
                            if pos not in visited and grid[x][y] == 1:
                                visited.add(pos)
                                stack.append(pos)

        return max(num_islands,area)