class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  
        memo = {}
        
        def dp(i):
            if i < 0:
                return True
            
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return dp(len(s) - 1)