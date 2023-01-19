# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def insert(node, x):
            if x > node.val:
                if node.right:
                    insert(node.right, x)
                else:
                    node.right = TreeNode(x)
            else:
                if node.left:
                    insert(node.left, x)
                else:
                    node.left = TreeNode(x)
        
        root = TreeNode(preorder[0])
        for num in preorder[1:]:
            insert(root, num)
            
        return root