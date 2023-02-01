class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # The greatest common divisor must be a prefix of each string, so we can try all prefixes.
        
        (shorterStr, longerStr) = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        
        gcd = ""
        prefix = ""
        
        for s in shorterStr:
            
            prefix += s
            
            multiplicant, thisPrefixNotADivisorOfShorterStr = divmod(len(shorterStr), len(prefix))
            if not thisPrefixNotADivisorOfShorterStr and prefix*multiplicant == shorterStr:
                
                multiplicant, thisPrefixNotADivisorOfLongerStr = divmod(len(longerStr), len(prefix))

                if not thisPrefixNotADivisorOfShorterStr and prefix*multiplicant == longerStr:
                    gcd = prefix if len(prefix) > len(gcd) else gcd
        
        return gcd