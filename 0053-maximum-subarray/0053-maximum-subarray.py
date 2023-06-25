class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        subSum = 0 
        max_subSum = nums[0]
        for num in nums:
            
            subSum += num
            if subSum > max_subSum:
                max_subSum = max(max_subSum, subSum)
            if subSum < 0:
                subSum = 0
        return max_subSum