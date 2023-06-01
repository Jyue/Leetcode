class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        # # Reverse word if freqency of first word is larger than the last of word, 
        # if word.count(word[0]) > word.count(word[-1]):
        #     word = word[::-1]
            
        def dfs(r, c, ci):
            
            if ci == len(word):
                return True
            
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            
            if board[r][c] != word[ci]:
                return False
            
            curr = board[r][c]
            board[r][c] = "#" # Instead of using set to storage visited coordinates, modify the char on board directly, 
            a1 = dfs(r + 1, c, ci + 1)
            b1 = dfs(r - 1, c, ci + 1)
            c1 = dfs(r, c + 1, ci + 1)
            d1 = dfs(r, c - 1, ci + 1)
            board[r][c] = curr
            
            return a1 or b1 or c1 or d1
            
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                
        
        return False