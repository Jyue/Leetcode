class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1,numRows):
            # print(i)
            if i == 1:
                res.append([1,1])
                continue
            else:
                res.append([1] + [ res[i-1][j] + res[i-1][j+1] for j in range(i-1)] + [1])
    
        return res
            