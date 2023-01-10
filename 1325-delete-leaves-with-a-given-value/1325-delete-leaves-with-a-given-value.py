# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            
            # Base Case
            if not node:
                return None, False
            
            # Leaves node and == target     -> delete
            if not node.left and not node.right:
                if node.val == target:
                    return None, True
                else:
                    return node, False
                
            
            # Non Leaves node -> dfs
            deleted = False
            if node.left:
                node.left, left_deleted = dfs(node.left)
                if left_deleted:
                    deleted = True
                    
            if node.right:
                node.right, right_deleted = dfs(node.right)
                if right_deleted:
                    deleted = True
                    
            return node, deleted
        
        
        new_root, deleted = dfs(root)
        while deleted:
            new_root, deleted = dfs(new_root)
        
        if not new_root:
            return None
        
        return new_root
            