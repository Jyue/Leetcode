class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        # 遍歷 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 每發現一個島嶼，島嶼數量+1
                    res += 1
                    # 然後使用DFS將島嶼淹了
                    self.dfs(grid, i, j)
        return res

    # 從 (i, j) 開始，將與之相鄰的陸地都變成海水
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引邊界
            return
        if grid[i][j] == '0':
            # 已經是海水了
            return
        # 將 (i, j) 變成海水
        grid[i][j] = '0'
        # 淹沒上下左右的陸地
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)