class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        n = len(s)
        
        # Build children
        children = [[] for _ in range(n)]
        for i in range(1,len(parent)):
            children[parent[i]].append(i)
        # print(children)
        
        
        longest_path = 1
        
        def dfs(node):
            # print("node",node)
            nonlocal longest_path

            # While examing the children, 
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node 
            # in the sub-tree rooted at this node.
            
            max1 = max2 = 0
            for child in children[node]:
                child_path = dfs(child)
                if s[child] != s[node]:
                    
                    if child_path > max1:
                        max2 = max1
                        max1 = child_path
                    elif child_path > max2:
                        max2 = child_path
            # print(node,max1,max2)
            path = 1 + max1 + max2
            
            longest_path = max(longest_path, path)
            return max1 + 1
        
        
        dfs(0)
        
        return longest_path