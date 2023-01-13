# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        ans = []
        
        def subtreeSum(node):
            nonlocal freq
            
            if not node:
                return 0
            
            if not node.left and not node.right:
                totalSum = node.val
            else:
                leftSum = subtreeSum(node.left) if node.left else 0
                rightSum = subtreeSum(node.right) if node.right else 0
                totalSum = leftSum + rightSum + node.val
            
            # print(node.val,totalSum)
            
            if totalSum not in freq:
                freq[totalSum] = 1
            else:
                freq[totalSum] += 1
            
            return totalSum
        
        subtreeSum(root)
        maxFreq = max(freq.values())
        # print(freq)
        for subSum in freq:
            if freq[subSum] == maxFreq:
                ans.append(subSum)
                
        return ans