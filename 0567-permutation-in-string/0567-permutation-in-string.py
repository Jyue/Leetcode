
class Solution:
    def checkInclusion(self, s1, s2):
        s1Count, s2Count = [0]*26, [0]*26
        n = len(s1)
        for i in range(n):
            s1Count[ord(s1[i]) - ord('a')] += 1
            
        
        for i in range(len(s2)):
            print("s2Count:",s2Count)
            s2Count[ord(s2[i]) - ord('a')] += 1
            if i >= n:
                s2Count[ord(s2[i-n]) - ord('a')] -= 1
            if s1Count == s2Count:
                return True
        return False