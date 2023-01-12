class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
             
        # Build adj list
        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # print(adj)
        
        
        ans = [0] * n
        
        
        def countLabels(node, parent) -> List[int]:
            # print(node)
            count = [0]*26
            
            count[ord(labels[node])-ord('a')] += 1
            
            # if node not in adj:
            #     return count


            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                count = [sum(i) for i in zip(count, countLabels(neighbor, node))]  

            # Build ouput
            ans[node] = count[ord(labels[node])  - ord('a')]
            
            return count
            
       
        
        countLabels(0 , -1)
        
        return ans
        