class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        
        def dfs(node, visited, dist):
            
            visited[node] = True

            next = edges[node]
            if next >= 0 and not visited[next]:
                
                dist[next] = 1 + dist[node]
                dfs(next, visited, dist)
                

            

        minLength1 = [-1]*len(edges)
        minLength1[node1] = 0
        dfs(node1, [False]*len(edges), minLength1)
        
        minLength2 = [-1]*len(edges)
        minLength2[node2] = 0
        dfs(node2, [False]*len(edges), minLength2)

        # print(minLength1, minLength2)
        
        Min = float(inf)
        target = -1
        
        for dst in range(len(edges)):
            if minLength1[dst] >= 0 and minLength2[dst] >= 0:
                longerLength = max(minLength1[dst], minLength2[dst])
                if longerLength < Min:
                    Min = longerLength
                    target = dst
            
                
            # print(Min)
            
            
            
        return target
        