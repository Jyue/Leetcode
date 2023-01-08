# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursive
        def isMirror(r1,r2):
            if (r1 == None and r2 == None):
                return True
            if (r1 == None or r2 == None):
                return False
 
            return (r1.val == r2.val) and isMirror(r1.right, r2.left) and isMirror(r1.left, r2.right)
            
            
        return isMirror(root,root)