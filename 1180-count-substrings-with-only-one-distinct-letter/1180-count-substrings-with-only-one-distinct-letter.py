class Solution:
    def countLetters(self, s: str) -> int:
        # print(s)
        
        if not s:
            return
        
        if len(s) == 1:
            return 1
        
        j = 0
        while j < len(s) - 1:
            # print(j)
            if s[j+1] == s[0]:
                j += 1
            else:
                break
        # print("Fianl j",j)        
        # print(sum(range(j+2)))      
                
        return sum(range(j+2)) + self.countLetters(s[j+1:]) if j != len(s)-1 else sum(range(j+2))