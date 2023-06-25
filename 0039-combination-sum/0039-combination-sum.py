class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0:
                return  True # backtracking
            if target == 0:
                res.append(path)
                return False
            for i in range(index, len(candidates)):
                if dfs(target-candidates[i], i, path+[candidates[i]]): break
        
        dfs(target, 0, [])
        return res