

class Solution:
    def checkInclusion(self, s1, s2):
        if(len(s1)>len(s2)):
            return False
        
        cntr, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
            if i >= w and s2[i-w] in cntr: 
                cntr[s2[i-w]] += 1

            if all([cntr[i] == 0 for i in cntr]): # see optimized code below
                return True

        return False