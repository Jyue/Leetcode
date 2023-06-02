class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        #res = []
        for point in points:
            distance = sqrt((point[0]**2)+(point[1]**2))
            if len(heap) < k:
                heapq.heappush(heap,[-distance,point])
            elif distance < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,[-distance,point])
        print(heap)
        
        # for i in range(k):
        #     x = heapq.heappop(heap)
        #     res.append(x[1])
        
        return [heapq.heappop(heap)[1] for i in range(k)]