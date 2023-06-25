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
            
            
            if nums[mid] < nums[r]: # 表示右側正常排序
                r = mid - 1  # 則代表反轉處在左側
            else:# 表示左側正常排序
                l = mid + 1# 則代表反轉處在右側