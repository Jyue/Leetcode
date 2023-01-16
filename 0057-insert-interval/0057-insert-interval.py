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
        
        # Binary Search
        def binary_search_start(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                if arr[mid] ==  x:
                    return mid
                elif x > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                    

            # If we reach here, then the element was not present
            return high
        
        # Binary Search
        def binary_search_end(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                if arr[mid] ==  x:
                    return mid
                elif x > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
                    
             # If we reach here, then the element was not present
            return low
        
        
        res = []
        hasPutNewInterval = 0
        
        
        start = binary_search_start([interval[0] for interval in intervals],newInterval[0])
        print(start)
        
        end = binary_search_end([interval[1] for interval in intervals],newInterval[1])
        print(end)
        
        
        if start != -1:
            if checkOverlaps(newInterval, intervals[start]):
                newInterval = mergeOverlaps(newInterval, intervals[start])
                start -= 1
            
        if end != len(intervals):
            if checkOverlaps(newInterval, intervals[end]):
                newInterval = mergeOverlaps(newInterval, intervals[end])
                end += 1
        
        
        
        
        print("Final start and end",start,end)
        
        if start != -1:
            front = intervals[:start+1]
        else:
            front = []
            
        if end != len(intervals):
            tail = intervals[end:]
        else:
            tail = []
            
        
        print(front, [newInterval], tail)
        
        return(front + [newInterval] + tail)
#         for interval in intervals:
#             if not hasPutNewInterval:
#                 print(newInterval,interval,checkOverlaps(newInterval,interval))
#                 if checkOverlaps(newInterval, interval) == False:
#                     if newInterval[0] < interval[0]:
#                         res.append(newInterval)
#                         hasPutNewInterval = 1
#                         res.append(interval)
#                     elif interval[0] < newInterval[0]:
#                         res.append(interval)
#                         #res.append(newInterval)
#                 else:   # Overlaps detect
#                     newInterval = mergeOverlaps(newInterval, interval)
#                     # print(newInterval)
#             else:
#                 res.append(interval)
                
#         if not hasPutNewInterval:
#             res.append(newInterval)
        
        return(res)
                