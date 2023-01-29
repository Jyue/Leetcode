class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuyPoint = float(inf)
        maxProfit = 0
        for price in prices:
            if price < bestBuyPoint:
                bestBuyPoint = price
            else:
                maxProfit = max( price - bestBuyPoint, maxProfit )
                
        return maxProfit