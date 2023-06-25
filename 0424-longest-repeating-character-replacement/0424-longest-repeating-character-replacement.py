class Solution:
     def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq = Counter()
        maxlen = 0
        for r in range(len(s)):
    
            freq[s[r]] +=  1
             
           
            cur_len = r - l + 1
            
            # 如果 replacement cost <= k : 更新最長字串長度
            if cur_len - max(freq.values()) <= k:  
                maxlen = max(maxlen, cur_len)
            # 如果 replacement cost > k: 無法再延長了，所以要把左界左移
            else:                             
                freq[s[l]] -= 1                 
                l += 1
               
        return maxlen