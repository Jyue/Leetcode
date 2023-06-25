class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-Inf")
        curr_sum = 0
        for el in nums:
            curr_sum += el
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum