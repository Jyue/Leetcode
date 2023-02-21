class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            
            if right == left:
                return nums[left]
            
            mid = (left +right)//2
            halfLen = mid - left
            if halfLen % 2 == 0: # halfLen is even
                if nums[mid] == nums[mid-1]:
  
                    right = mid - 2
                elif nums[mid] == nums[mid+1]:

                    left = mid + 2
                else:
                    return nums[mid]
            else:       # halfLen is odd
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                elif nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    return nums[mid]
        
        return nums[left]
        