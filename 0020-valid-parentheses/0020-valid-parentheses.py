class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3
    
# 1. 如果是 左括號 => 加到 stack
# 2. 如果是 右括號 且 (1)stack 是空的(代表沒有matching的左括號) (2)或是 左括號不 match => return False
# 3.  最後 check stack 中是否還有殘留的左括號
                    