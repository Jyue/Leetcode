class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        block = defaultdict(list)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in block[3*(i//3)+(j//3)]:
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                block[3*(i//3)+(j//3)].append(board[i][j])
                # print(dict(row),dict(col),dict(block))
                # print(dict(block))
                
        return True
                

            