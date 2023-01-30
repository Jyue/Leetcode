class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] *38
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        if n == 0 or n == 1 or n == 2:
            return dp[n]
        
        i = 3
        
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            i += 1
            
        return dp[n]