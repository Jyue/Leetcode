class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        j = 0
        product = 1
        
        if k <= 1:
            return 0
        
        # for i in range(len(nums)) :
            
        product = 1

        for j in range(i, len(nums)) :

            product = product * nums[j]


            while product >= k:
                product /= nums[i]
                i += 1
            count += j - i + 1
            # if product < k:
            #        count += 1  
            # else:
            #     break

        return count