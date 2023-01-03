class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for pair in zip(*strs):
            # print(pair,tuple(sorted(pair)))
            if pair != tuple(sorted(pair)):
                count += 1
        return count