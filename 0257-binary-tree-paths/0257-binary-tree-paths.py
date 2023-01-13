# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node):
            
            if not node.left and not node.right:
                return [str(node.val)]
            if not node:
                return
            
            res = []
            if node.left:
                for postfix in dfs(node.left):
                    res.append(str(node.val)+"->"+ postfix)
            if node.right:
                for postfix in dfs(node.right):
                    res.append(str(node.val)+"->"+postfix)
                
            
            return res
         
        
        return dfs(root)