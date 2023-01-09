class Solution:
    def confusingNumber(self, n: int) -> bool:
        string = list(str(n))
        
        length = len(string)
        new_string = [""]*length
        
        # Rule
        rotateMap = {"6":"9", "9":"6"}
        invalid = {"2","3","4","5","7"}
        
        for i in range(length):
            if string[i] in invalid:
                return False
            elif string[i] in rotateMap:
                new_string[length-i-1] = rotateMap[string[i]]
            else:
                new_string[length-i-1] = string[i]
              
        
        
        return True if new_string != string else False
            