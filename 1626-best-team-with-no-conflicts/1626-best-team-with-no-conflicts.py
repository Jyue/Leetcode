class Solution:
    def findMaxScore(self, players):
        n = len(players)
        ans = 0
        dp = [0]*n
        
        # Initially, the maximum score for each player will be equal to the individual scores.
        for i, player in enumerate(players):
            dp[i] = player[1]
 
        ans = max(ans, max(dp))
        
        for i in range(n):
            for j in (range(i-1, -1, -1)):
                # If the players j and i could be in the same team.
                if players[i][1] >= players[j][1]:
                    # Update the maximum score for the ith player.
                    dp[i] = max(dp[i], players[i][1] + dp[j])
            ans = max(ans, dp[i])
        
        return ans
        
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(list(zip(ages, scores)), key = lambda x: (x[0],x[1]))
        
        # print(players)
        
        return self.findMaxScore(players)