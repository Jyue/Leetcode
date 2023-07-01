class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        
        if n == 1:
            return True
        
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            # 如果碰到0，卡住
            if farthest <= i:
                return False
            elif farthest >= n - 1:
                 return True
        return farthest >= n - 1
  