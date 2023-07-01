class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                # 超出索引邊界
                return 1
            if grid[i][j] == 1:
                return 0
            grid[i][j] = 1
            
            return dfs(i + 1, j) | dfs(i, j + 1) | dfs(i - 1, j) | dfs(i, j - 1)
            # result = 0
            # result |= dfs(i + 1, j)
            # result |= dfs(i, j + 1)
            # result |= dfs(i - 1, j)
            # result |= dfs(i, j - 1)
            # return result
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    notClosed = dfs(i, j)
                    print(i,j,notClosed)
                    count += 1 - notClosed
                    
        return count

        