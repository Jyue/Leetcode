class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        count = 0
        m, n = len(grid), len(grid[0])

        def detectEdge(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                # 超出索引邊界
                return True
            if grid[i][j] == 1:
                return False
            grid[i][j] = 1
            
        
            # 注意不可用 or ，否則若有一者回傳True，後面不會被執行!!
            return detectEdge(i + 1, j) | detectEdge(i, j + 1) | detectEdge(i - 1, j) | detectEdge(i, j - 1)
         
            # return result
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    notClosed = detectEdge(i, j)

                    count += 1 - notClosed
                    
        return count

        