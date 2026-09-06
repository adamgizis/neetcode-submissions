class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def valid_moves(x,y):
            result = []
            if x+1 < len(board):
                result.append((x+1,y))
            if x-1 >= 0:
                result.append((x-1,y))
            if y+1 < len(board[0]):
                result.append((x,y+1))
            if y-1 >= 0:
                result.append((x,y-1))
            return result
            
        def dfs(index,i,j ):
            if word[index] != board[i][j]:
                return False
            
            if (word[index] == board[i][j]) and (index == len(word) - 1):
                return True

            for pos in valid_moves(i,j):
                if pos not in cur:
                    cur.add(pos)
                    if dfs(index + 1, pos[0], pos[1]):
                        return True
                    cur.remove(pos)
                
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = set()
                cur.add((i,j))
                if dfs(0,i,j) == True:
                    return True


        return False


            
                








        return false
        