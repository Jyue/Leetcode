class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
    
        
        # Kadane's Algorithm
        cur_max = 0
        cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        Sum = 0
         
        for num in nums:
            cur_max += num
            cur_min += num
            Sum += num
            max_sum = max(cur_max, max_sum)
            min_sum = min(cur_min, min_sum)
            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0
        print(max_sum, min_sum)
        return max_sum if Sum == min_sum else max(max_sum, Sum - min_sum)