class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        heapq.heapify(intervals)
        max_till_now = 0
        
        while intervals:
            start, end = heapq.heappop(intervals)
            if start < max_till_now:
                return False
            else:
                max_till_now = max(max_till_now, end)
             
        return True