# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):  # Return [How many target finded, the lowestCommonAncestor(TreeNode)]
            # print(node)
            if not node:
                return (0,None)
            
            if not node.left and not node.right:
                # print(node.val,"is a leaf",node.val == p or node.val == q)
                return (1,None) if (node.val == p.val or node.val == q.val) else (0,None)
            
            
            
            left, leftAncestorFind = dfs(node.left)
            right, rightAncestorFind = dfs(node.right)
            
            if leftAncestorFind or rightAncestorFind:
                # print(node.val,"has found target")
                if leftAncestorFind:
                    return (2,leftAncestorFind)
                else:
                    return (2,rightAncestorFind)
                
            
            if node.val == p.val or node.val == q.val:
                count = 1 + left + right
            else:
                count = left + right
            
            # print(node.val, count)
            return (2,node) if count == 2 else (count,None)
   
                
        # print(dfs(root))
        # return 0
        _,lowestCommonAncestor = dfs(root)
        # print(lowestCommonAncestor)
        
        return lowestCommonAncestor