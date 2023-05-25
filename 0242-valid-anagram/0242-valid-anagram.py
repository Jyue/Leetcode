class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = defaultdict(int)
        for c1 in s:
            hashmap[c1] += 1
        for c2 in t:
            if c2 in hashmap and hashmap[c2] > 0:
                hashmap[c2] -= 1
            else:
                return False
        return True
            