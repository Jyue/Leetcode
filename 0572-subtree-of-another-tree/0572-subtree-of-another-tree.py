# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(r1,r2):
            # If any one Node is Empty, both should be Empty
            if r1 == None or r2 == None:
                return r1 is None and r2 is None
            return r1.val == r2.val and isIdentical(r1.left, r2.left) and isIdentical(r1.right, r2.right)
        
        # Preorder Traversal
        def preorderTraversal(node):
            if node is None:
                return False
            elif isIdentical(node, subRoot):
                return True
            
            
            return preorderTraversal(node.left) or preorderTraversal(node.right)
        
        return preorderTraversal(root)
        