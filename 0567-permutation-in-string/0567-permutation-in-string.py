

class Solution:
    def checkInclusion(self, s1, s2):
        l = 0
        for r in range(len(s2)):
            if r-l+1 == len(s1):
                if sorted(s2[l:r+1]) == sorted(s1):
                    return True
                else:
                    l+=1
        return False