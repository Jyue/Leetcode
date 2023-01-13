class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            # print(i)
            if i == 0:
                res.append([1])
                continue
            elif i == 1:
                res.append([1,1])
                continue
            else:
                res.append([1] + [ res[i-1][j] + res[i-1][j+1] for j in range(i-1)] + [1])
    
        return res
            