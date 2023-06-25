class Solution(object):
    def minWindow(self, strFull, strChars):

        countRemaining = len(strChars)
        ansStart,ansEnd = 0, float('inf')
        targCharsRemaining = collections.defaultdict(int)
        
        for ch in strChars:
            targCharsRemaining[ch] +=1
        
        startIndex = 0

        for endIndex, ch in enumerate(strFull, 1):
            
            if targCharsRemaining[ch] > 0:
                countRemaining -= 1
                
            targCharsRemaining[ch] -=1
            
            if countRemaining == 0:
                
                while targCharsRemaining[strFull[startIndex]] < 0:
                    targCharsRemaining[strFull[startIndex]] += 1
                    startIndex +=1
                    
                if endIndex - startIndex < ansEnd - ansStart:
                    ansStart, ansEnd = startIndex, endIndex
                    
                targCharsRemaining[strFull[startIndex]] += 1
                startIndex += 1
                countRemaining += 1
                
        return strFull[ansStart:ansEnd] if ansEnd != float('inf') else ""