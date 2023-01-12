class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zeros = 0
        total = 0
        
        m = len(num1)
        n = len(num2)
        
        for j in range(n):
            
            # Multiply one digit
            res = 0
            for i in range(m):
                res += int(num1[i]) * int(num2[j]) * 10**(m - i - 1)
            total += res * 10 **(n - j - 1)
            
        return str(total)
            