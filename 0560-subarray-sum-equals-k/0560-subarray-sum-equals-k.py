class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulateSumFreq = {}
        accumulateSum = 0
        count = 0
        for num in nums:
            accumulateSum += num
            # print(accumulateSum)
            
            
            # print(accumulateSumFreq)
            if accumulateSum == k:
                # print("+1")
                count += 1
            if (accumulateSum - k) in accumulateSumFreq:
                # print("+n")
                count += accumulateSumFreq[accumulateSum - k]
                
            if accumulateSum not in accumulateSumFreq:
                accumulateSumFreq[accumulateSum] = 1
            else:
                accumulateSumFreq[accumulateSum] += 1
        
        return count
        