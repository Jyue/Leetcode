class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        
        projects = list(zip(capital, profits))
        projects.sort()
        # print(projects)
        
        n = len(projects)
        maxHeap = []
        idx = 0
        
        for i in range(k):
            while idx < n and projects[idx][0] <= w:
                heappush(maxHeap, -projects[idx][1])
                idx += 1
            if not maxHeap:
                break
            w += -heappop(maxHeap)
        return w