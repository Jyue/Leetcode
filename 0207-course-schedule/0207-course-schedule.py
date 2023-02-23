class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def hasCycle(v):
            
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True
    
            # Set state to -1
            state[v] = -1
            
            for i in adjList[v]:
                if hasCycle(i):
                    return True
            
            
            
            state[v] = 1
            return False
        
        
        
        
        adjList = [[] for _ in range(numCourses)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in prerequisites:
            # if c1 == c2:
            #     return False
            adjList[c2].append(c1)
            
        
        print(adjList)
    
        for v in range(numCourses):
            state = [0] * numCourses
            # print(v, hasCycle(v))
            if hasCycle(v):
                return False
        return True 
            