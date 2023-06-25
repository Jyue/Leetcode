class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def backtracking(target, index, path):
            if target < 0:
                return True # backtracking
            if target == 0:
                res.append(path)
                return True
            for i in range(index, len(candidates)):
                if backtracking(target-candidates[i], i, path+[candidates[i]]): 
                    break
        
        backtracking(target, 0, [])
        return res