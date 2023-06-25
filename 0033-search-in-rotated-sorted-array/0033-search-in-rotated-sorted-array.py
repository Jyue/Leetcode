class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        
        if n == 1:
            return 0 if nums[0] == target else -1
        if n == 2:
            if target not in nums:
                return -1
            else:
                return 0 if nums[0] == target else 1
        
        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] == target:
                return mid
            
            elif target >  nums[mid]:# 照理說往右找
                # 特殊狀況: target在左側反轉處
                if nums[l] > nums[r] and target > nums[r] and nums[l] > nums[mid]:
                    r = mid - 1
                else:# 正常情況
                    l = mid + 1
            else:# 照理說往左找
                # 特殊狀況: target在右側反轉處
                if nums[l] > nums[r] and target < nums[l] and nums[r] < nums[mid]:
                    l = mid + 1
                else:# 正常情況
                    r = mid - 1
        return -1