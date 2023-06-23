# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            inorder_index = inorder_index_map[root_val]
            
            preorder_index += 1
            root.left = helper(left, inorder_index - 1)
            root.right = helper(inorder_index + 1, right)
            return root
            
        
        preorder_index = 0
        inorder_index_map = {}
        for index,value in enumerate(inorder):
            inorder_index_map[value] = index
            
        return helper(0, len(preorder) - 1)  