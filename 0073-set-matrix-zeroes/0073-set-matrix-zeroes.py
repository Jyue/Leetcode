class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # 先確認第一列和第一行清0狀況，並將之記錄在左上角的欄位。之後用第一列和第一行當作 flag
        
        # Step1: flag常數用來確認第一列和第一行最後是否為 0
        # 0: 不改，1: 第一列和第一行清0，2: 第一row清0，3: 第一col清0
        flag = 0
        
        
        if matrix[0][0] == 0:
            flag = 1
        else:
            for i in range(n):
                if matrix[0][i] == 0:
                    flag = 2
                    break
            for j in range(m):
                if matrix[j][0] == 0:
                    if flag == 2:
                        flag = 1
                    else:
                        flag = 3
                    break   
        # Step2: 第一列和第一行當flag，確認每一行每一列是否清0
        # 0: 清0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # Step3: 根據左上角，將每一行每一列清0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for k in range(1,n):
                    matrix[i][k] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for k in range(1,m):
                    matrix[k][j] = 0
                
        # Step4: 根據flag常數，將第一列和第一行清0
        if flag == 1 or flag == 2:
            for i in range(n):
                matrix[0][i] = 0
        if flag == 1 or flag == 3:
            for i in range(m):
                matrix[i][0] = 0
            