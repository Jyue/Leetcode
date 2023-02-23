class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        
        
        # BFS method        
       
        
            
        
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    
                    grid[r][c] = '0' # mark as visited
                    
                    neighbors = []
                    neighbors.append([r, c])
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if (row - 1 >= 0 and grid[row-1][col] == '1'): 
                            neighbors.append([row-1, col])
                            grid[row-1][col] = '0'
                        if (row + 1 < nr and grid[row+1][col] == '1'):  
                            neighbors.append([row+1, col])
                            grid[row+1][col] = '0'
                        if (col - 1 >= 0 and grid[row][col-1] == '1'):  
                            neighbors.append([row, col-1])
                            grid[row][col-1] = '0'
                        if (col + 1 < nc and grid[row][col+1] == '1'):  
                            neighbors.append([row, col+1])
                            grid[row][col+1] = '0'
        return num_islands