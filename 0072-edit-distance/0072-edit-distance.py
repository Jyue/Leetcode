class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)+1
        n = len(word2)+1
        dp = [[0]*(n) for _ in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = i
                elif i == 0:
                    dp[i][j] = j
                    
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1 , dp[i-1][j] + 1, dp[i][j-1] + 1)
            
        # print(dp)
        return dp[m-1][n-1]