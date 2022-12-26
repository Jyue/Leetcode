def binarySearch(nums: List[int], target: int):
    left = 0
    right = len(nums) -1
    
    while (left <= right):
        mid = (left+right) // 2
        if target < nums[mid]:
            right = mid -1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return nums[mid]
    return float("-inf")
    
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)):
            i_val = sorted_nums[i]
            j_val = binarySearch(sorted_nums[i+1:],target-sorted_nums[i])
            if j_val != float("-inf"):
                break
      
        print(i_val,j_val)
        
        indices = []
        for i in range(len(nums)):
            if nums[i] in [i_val,j_val]:
                indices.append(i)
                if len(indices) == 2:
                    return indices
            