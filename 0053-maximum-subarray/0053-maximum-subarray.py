class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray