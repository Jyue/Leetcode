class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        cntrP = Counter(p)
        cntrS = Counter(s[:len(p)])
        
        i = 0
        j = len(p) - 1
        
        # print(cntrP,cntrS)
        
        while j <= len(s) - 1:
            if cntrP == cntrS:
                res.append(i)
            
            if j == len(s) - 1:
                break
            
            cntrS[s[i]] -= 1
            i += 1
            
            j += 1
            cntrS[s[j]] += 1
            
        return res