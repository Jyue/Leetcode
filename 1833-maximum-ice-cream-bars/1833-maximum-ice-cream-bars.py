class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        count = 0
        
        if costs[0] > coins:
            return count
        
        for cost in costs:
            if coins > 0 and coins >= cost:
                coins -= cost
                count += 1
            else:
                return count
        print(coins)
        return count
            
            