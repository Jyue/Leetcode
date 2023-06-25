class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = []
        for i in range(len(nums)):
            if not f or nums[i] > f[-1]:
                f.append(nums[i])
            else:
                pos = bisect.bisect_left(f, nums[i])
                f[pos] = nums[i]
        return len(f)