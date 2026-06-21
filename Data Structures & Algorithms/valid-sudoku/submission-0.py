class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        block = {}
        for i in range(0,9):
            block[i] = set()


        for i in range(len(board)):
            if i not in row:
                row[i] = set()
            for j in range(len(board[0])):
                if j not in col:
                    col[j] = set()
                val = board[i][j]
                if val == ".":
                    continue
                if val in row[i]:
                    return False
                if val in col[j]:
                    return False
                b =(i // 3) + ((j // 3)*3)
                if val in block[b]:
                    return False

                row[i].add(val)
                col[j].add(val)
                block[b].add(val)

                


        

        return True
                
    