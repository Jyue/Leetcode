class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        self.meeting_array = [0]*1000001
        self.max_end_time = 0
        for interval in intervals:
            start, end = interval[0],interval[1]
            self.meeting_array[start] += 1
            self.meeting_array[end] -= 1
            if end > self.max_end_time:
                self.max_end_time = end
        meeting_count = 0
        for i in range(self.max_end_time):
            meeting_count += self.meeting_array[i]
            if meeting_count > 1:
                return False
        return True