class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # Let dp[n] be the number of ways that n people can handshake.
        dp = [0] * (numPeople + 1)
        dp[0] = dp[1] = dp[2] = 1
        m = 1000000007
        for i in range(4, numPeople+1):
            if i % 2 == 0:
                for k in range(1,i+1):
                    if k % 2 == 0:
                        subProblem1 = k - 2
                        subProblem2 = i - k
                        # print(i, dp[subProblem1], dp[subProblem2])
                        dp[i] += dp[subProblem1] * dp[subProblem2]
                        dp[i] %= m
                
        # print(dp)
        return dp[-1]