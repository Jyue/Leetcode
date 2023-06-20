class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n= len(board), len(board[0])
        visited = [[0] * n for i in range(m)]

        def backtrack(r, c, w_indx):
            if w_indx == len(word):
                return True

            if (min(r, c) < 0
                or r == m
                or c == n
                or word[w_indx] != board[r][c]
                or visited[r][c]
            ):
                return False

            visited[r][c] = 1
            res = (
                backtrack(r, c + 1, w_indx + 1)
                or backtrack(r, c - 1, w_indx + 1)
                or backtrack(r + 1, c, w_indx + 1)
                or backtrack(r - 1, c, w_indx + 1)
            )
            visited[r][c] = 0
            return res

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False