def clean(s: str):
    return re.sub(r'[\W_]', '', s.lower())

class Solution:
  
    def isPalindrome(self, s: str) -> bool:
        cleanStr = clean(s)
       
        
        if cleanStr == "":
            return True 
    
        for i in range(len(cleanStr)//2):
            if cleanStr[i] != cleanStr[len(cleanStr)-1-i]:
                return False
        return True
        