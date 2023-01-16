class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Tell if two given intervals overlaps
        def checkOverlaps(me,interval):
            start = me[0]
            end = me[1]
            case1 = interval[0] <= start <= interval[1]
            case2 = interval[0] <= end <= interval[1]
            case3 = start <= interval[0] and interval[1] <=  end
            return True if case1 or case2 or case3 else False
        
        # Merge two overlapping intervals
        def mergeOverlaps(interval1,interval2):
            return [min(interval1[0],interval2[0]), max(interval1[1],interval2[1])]
        
        
        res = []
        hasPutNewInterval = 0
        for interval in intervals:
            if not hasPutNewInterval:
                print(newInterval,interval,checkOverlaps(newInterval,interval))
                if checkOverlaps(newInterval, interval) == False:
                    if newInterval[0] < interval[0]:
                        res.append(newInterval)
                        hasPutNewInterval = 1
                        res.append(interval)
                    elif interval[0] < newInterval[0]:
                        res.append(interval)
                        #res.append(newInterval)
                else:   # Overlaps detect
                    newInterval = mergeOverlaps(newInterval, interval)
                    # print(newInterval)
            else:
                res.append(interval)
                
        if not hasPutNewInterval:
            res.append(newInterval)
        
        return(res)
                