class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def helper(matrix, start, m, n ,res):
            print(start,m,n)
            
            round = []
            
            if start +1 > m or start+1 > n:
                return
            
            if m - start == 1 and n - start == 1:
                res.append(matrix[start][start])
                return
       

            # Right
            round = matrix[start][start:n]
            
            # Down
            if m - start >= 3:
                for i in range(start + 1,m-1):
                    round.append(matrix[i][n-1])
            
            # Left
            if m - start >= 2:
                round += matrix[m-1][start:n][::-1]
            
            # Up
            if n - start >= 2 and m - start >= 3:
                for i in range(m-2,start,-1):
                    round.append(matrix[i][start])
        
            
            
            res += round
            # print(res)
            
            helper(matrix, start+1 ,m-1,n-1, res)
        
        
        
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        helper(matrix,0,m,n,res)
        return res