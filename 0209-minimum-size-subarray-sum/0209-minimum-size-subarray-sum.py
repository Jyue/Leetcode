class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        
        min_len = float(inf)
        
        sum = 0
        
        while j < len(nums):
            # print(i,j)
            sum += nums[j]
            # print(sum)
            
            if sum >= target:
                min_len = min(j - i + 1, min_len)
                
                sum = sum - nums[i] - nums[j]
                i += 1
                
#                 # Constrain from left
#                 while i < j:
#                     sum -= nums[i]
#                     i += 1
#                     # print(i,j)
#                     # print(sum)
#                     if sum >= target:
#                         min_len -= 1
#                         # print("min_len", min_len)
#                     else:
#                         break    # windowSize = min_len - 1
                
#                 # Move to right
                
#                 sum -= nums[i]
#                 i += 1
#                 j += 1
                
            else:
                j += 1
                
        # print(i,j)      
        # print("&min_len", min_len)
        return min_len if min_len != float(inf) else 0
                