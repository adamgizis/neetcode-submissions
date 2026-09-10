from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        def valid_neighbors(pos):
            r,c = pos
            results = []

            if r+1 < len(heights) and heights[r][c] <= heights[r+1][c]:
                results.append((r+1,c))
            if r-1 >= 0 and heights[r][c] <= heights[r-1][c]:
                            results.append((r-1,c))
            if c+1 < len(heights[0]) and heights[r][c] <= heights[r][c+1]:
                results.append((r,c+1))
            if c-1 >= 0 and heights[r][c] <= heights[r][c-1]:
                            results.append((r,c-1))
            
            return results
        def bfs(queue):
            visited = set(queue)
            while queue:
                pos = queue.popleft()
                for n in valid_neighbors(pos):
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
    
            return visited
        aq = deque()
        pacific_q = deque([(0, j) for j in range(len(heights[0]))] + 
                   [(i, 0) for i in range(len(heights))])
        atlantic_q = deque([(len(heights)-1, j) for j in range(len(heights[0]))] + 
                    [(i, len(heights[0])-1) for i in range(len(heights))])
        pacific = bfs(pacific_q)
        atlantic = bfs(atlantic_q)

        return list(atlantic & pacific)
            
        
        