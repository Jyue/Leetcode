class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        res = []
        for i in range(half):
            res.append(nums[i])
            res.append(nums[half+i])
        return res