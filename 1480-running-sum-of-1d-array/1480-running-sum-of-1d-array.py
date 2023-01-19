class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        for num in nums[1:]:
            runningSum.append(runningSum[-1]+num)
        return runningSum