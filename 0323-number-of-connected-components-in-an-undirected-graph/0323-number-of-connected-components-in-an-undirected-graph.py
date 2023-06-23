
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        count = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for n in adjlist[node]:
                if n not in visited:
                    dfs(n)
        
        for n in adjlist:
            if n not in visited:
                count += 1
                dfs(n)
        return count
