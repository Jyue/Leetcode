class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]:  i is the amount that we need to make up
        dp = [float('inf')]*(amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1