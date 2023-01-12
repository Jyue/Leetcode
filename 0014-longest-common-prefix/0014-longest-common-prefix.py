class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        
        min_len = 200
        
        for string in strs:
            if len(string) < min_len:
                min_len = len(string)
        
        print(min_len)
        
        if min_len == 0:
            return ""
        
        j = 0
  
        while j < min_len:
            char = strs[0][j]
            for string in strs[1:]:
                print(string[j],j)
                if string[j] != char:
                    return strs[0][:j]
            j += 1
            
        return strs[0][:j]
        
        