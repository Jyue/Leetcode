class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtracking(curr = [], curr_sum = 0, start = 0):
            nonlocal output
            if curr_sum == target:
                # 注意！！ make a deep copy of the current combination
                output.append(list(curr))
                return
            if curr_sum > target:
                return

            for i in range(start, n):
                curr.append(candidates[i])
                curr_sum += candidates[i]

                backtracking(curr, curr_sum, i)

                curr.pop()
                curr_sum -= candidates[i]
            
        n = len(candidates)
        
        backtracking()
        return output