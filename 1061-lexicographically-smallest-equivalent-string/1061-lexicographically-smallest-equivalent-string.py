class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if root_x < root_y:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y
            
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        uf = UnionFind(26)
        for c1,c2 in zip(s1,s2):
            uf.union(ord(c1)-ord('a') , ord(c2)-ord('a'))
            
        # print(uf.root)
        
        ans = ""
        for c in baseStr:
            ans += chr( (uf.find(ord(c) - ord('a'))) + ord('a'))
        return ans