class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def valid_island_neighbors(pos):
            r,c = pos
            result = []
            if r + 1 < len(board) and board[r+1][c] == "O":
                result.append((r+1,c))

            if r -1 >= 0 and board[r-1][c] == "O":
                result.append((r-1,c))

            if c + 1 < len(board[0]) and board[r][c+1] == "O":
                result.append((r,c+1))

            if c - 1 >= 0 and board[r][c-1] == "O":
                result.append((r,c-1))

            return result

        def is_edge(pos):
            r,c = pos
            if r in (0, len(board)-1):
                return True
            if c in (0, len(board[0])-1):
                return True
            return False




        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == "O":
                    island = []
                    stack = [(i,j)]
                    visited.add((i,j))
                    surronded = True
                    while stack != []:
                        pos = stack.pop()
                        island.append(pos)
                        if is_edge(pos):
                            print("here")
                            surronded = False
                        for n in valid_island_neighbors(pos):
                            if n not in visited:
                                stack.append(n)
                                visited.add(n)
                    if surronded:
                        for r,c in island:
                            board[r][c] = "X"
            
