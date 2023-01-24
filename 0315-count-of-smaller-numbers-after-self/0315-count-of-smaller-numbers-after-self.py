class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            nonlocal result
            mergeResult = []
            i = 0
            j = 0
            left.append([-float(inf),0])
            right.append([float(inf),0])
            while i < len(left) and j < len(right):
                if left[i][0] == float(-inf):
                    i += 1
                    break
                if left[i][0] <= right[j][0]:
                    mergeResult.append(left[i])
                    # left[i][1] += j
                    result[left[i][1]] += j
                    
                    i += 1
                    
                else:
                    mergeResult.append(right[j])
                    # for count in left:
                    #     count[1] += 1
                    j += 1
            
            if i < len(left) and left[i][0] != float(-inf):
                mergeResult += left[i: len(left) - 1]
            if j < len(right) and right[j][0] != float(inf):
                mergeResult += right[j: len(right) - 1]
               
            # print(result)
            # print(left, "----", right,"----------", mergeResult)
            # print()
            return mergeResult
            
        def mergesort(array):
            if len(array) < 2:
                return array
            mid = len(array) //2
            return merge(mergesort(array[:mid]), mergesort(array[mid:]))
        
        

        # print(len(nums))        
        result = [0] *len(nums)
        count = []
        
        for idx, num in enumerate(nums):
            count.append([num, idx])
        
        mergesort(count)
        # print(count)
        
    
        # return [x[1] for x in count]
        return result
        
        
        