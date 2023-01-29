class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        
        if len(costs) == 1:
            return min(costs[0])
        
        minCost = [[0,0,0] for _ in range(n)]
        minCost[0] = costs[0]
        
        for i in range(1, n):
            # red
            minCost[i][0] = min( costs[i][0] + minCost[i-1][1] , costs[i][0] + minCost[i-1][2])
            # blue
            minCost[i][1] = min( costs[i][1] + minCost[i-1][0] , costs[i][1] + minCost[i-1][2])
            # green
            minCost[i][2] = min( costs[i][2] + minCost[i-1][0] , costs[i][2] + minCost[i-1][1])
            
        return min(minCost[i])