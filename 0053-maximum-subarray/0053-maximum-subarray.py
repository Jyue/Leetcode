class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumMax = current = nums[0]
        
        for i in range(len(nums)-1):
            current = max(current+nums[i+1], nums[i+1])
            sumMax = max(current, sumMax)
        
        return sumMax