class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return(nums[0])
        if n == 2:
            return(min(nums))
        
        l = 0
        r = n -1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] - nums[mid-1] < 0:
                return nums[mid]
            elif nums[r] > nums[mid]:
                r = mid-1
            else:
                l = mid+1