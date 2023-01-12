class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])
        
        position = [0]*n

        
        for ball in range(n):
            # Rule
            i = 0
            j = ball
            entrance = "U"
            # print("ball",j)
            
            while i < m and 0 <= j < n:
                # print(i,j)
                if grid[i][j] == 1:
                    if entrance == "U":
                        j += 1
                        entrance = "L"
                    elif entrance == "L":
                        i += 1
                        entrance = "U"
                    elif entrance == "R":
                        position[ball] = -1
                        break
                    else:
                        break
                else:            # grid[i][j] == -1
                    if entrance == "U":
                        j -= 1
                        entrance = "R"
                    elif entrance == "R":
                        i += 1
                        entrance = "U"
                    elif entrance == "L":
                        position[ball] = -1
                        break
                    else:
                        break
            
            position[ball] = j if i == m and 0 <= j < n else -1
        
        return position
                