class Solution:
    def confusingNumberII(self, n: int) -> int:
        
        
        validNums = [0,1,6,8,9]
        mapping = {0: 0,1: 1,6: 9,8: 8, 9: 6}
        
        self.count = 0

        def helper(v, rotation,digit):
            if v: 
                if v != rotation: 
                    self.count += 1  
            for i in validNums: 
                if v*10 + i > n:
                    break 
                else:
                    helper(v*10+i, mapping[i]*digit + rotation, digit*10)
        
        helper(1,1, 10)
        helper(6,9,10)
        helper(8,8,10)
        helper(9,6,10)

        return self.count   
       
            