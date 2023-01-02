class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        res = 0
        substring  = []
        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
                count = count + 1
                
             
            else:
                res = max(res,count)
                substring = substring[(substring.index(s[i])+1):]
                substring.append(s[i])
                count = len(substring)
       
        return max(res,count)