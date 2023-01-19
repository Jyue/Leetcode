# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def findMaxHeight(node):
            if not node:
                return 0
            return 1 + max(findMaxHeight(node.left), findMaxHeight(node.right))
        
        def dfs(node, depth):
            nonlocal ans, H
            if not node.left and not node.right and depth == H:
                # print(node.val)
                ans += node.val
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        
        
        H = findMaxHeight(root)
        ans = 0
        dfs(root,1)
        return ans
        
        