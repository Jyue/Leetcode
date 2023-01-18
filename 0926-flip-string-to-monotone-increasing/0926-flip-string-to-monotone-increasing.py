class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left1 = 0
        right0 = s.count("0")
        
        minFlip = left1 + right0
        for i in range(len(s)):
            if s[i] == "0":
                right0 -= 1
            else:
                left1 += 1
                
            minFlip = min(minFlip, right0 + left1)
 
            
        return minFlip
        