class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        #res = []
        for i, point in enumerate(points):
            distance = (point[0]**2)+(point[1]**2)
            if len(heap) < k:
                heapq.heappush(heap,[-distance,i])
            elif distance < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,[-distance,i])
        print(heap)
        
        # for i in range(k):
        #     x = heapq.heappop(heap)
        #     res.append(x[1])
        
        return [points[heapq.heappop(heap)[1]] for i in range(k)]