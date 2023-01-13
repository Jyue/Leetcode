# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longestPath = 0
        
        def dfs(node):
            nonlocal longestPath
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            
            left_path = 0
            right_path = 0
            
            if node.left:
                tmp_path = dfs(node.left)
                if node.left.val == node.val:
                    left_path = tmp_path + 1
            if node.right:
                tmp_path = dfs(node.right)
                if node.right.val == node.val:
                    right_path = tmp_path + 1
            # print(node.val,left_path,right_path)
            longestPath = max(longestPath, left_path + right_path)
            # print(longestPath)
            return max(left_path,right_path)
        
        dfs(root)
        return longestPath
            
            