class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = {char: 0 for char in 'abc'}
        i = 0
        n = len(s)
        for j in range(n):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            # print(i,j)
            res += i
                
        return res
                