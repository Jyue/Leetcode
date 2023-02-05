class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(curr = [], first = 0):
            if len(curr) == len(nums):
                output.append(curr[::])
                # print("Append to ouput",curr)
                return
            
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                
                curr.append(nums[i])
                backtracking(curr)
                curr.pop()
                # print("pop",curr)
            
        n = len(nums)
        output = []
        backtracking()
        return output