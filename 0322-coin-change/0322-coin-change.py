class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: 組成金額i的最少coin數
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                # 使用當前的coin來製成金額i，我們可以:
                # 使用 製成金額i-coin的最小硬幣數量 並將其加1（以考慮當前的硬幣），
                # 或者我們可以使用 其他面額製成金額i的最小硬幣數量。
                dp[i] = min(dp[i], dp[i-coin]+1)
                # print("coin:",coin,"   i:", i ,dp)

        return dp[amount] if dp[amount] != float('inf') else -1