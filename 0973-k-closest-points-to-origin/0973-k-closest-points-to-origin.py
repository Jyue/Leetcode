class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            heapq.heappush(heap,[sqrt((point[0]**2)+(point[1]**2)),point])
        # print(heap)
        for i in range(k):
            x = heapq.heappop(heap)
            # print(x)
            res.append(x[1])
        # print(res)
        return res