# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if not node.left and not node.right:
                return [str(node.val)]
            if not node:
                return

            res = []
            if node.left:
                for postfix in dfs(node.left):
                    res.append(str(node.val)+ postfix)
            if node.right:
                for postfix in dfs(node.right):
                    res.append(str(node.val)+postfix)


            return res

        
        # print(dfs(root))
        sum = 0
        for num in dfs(root):
            sum += int(num)
        
        return sum
        
        
        
        
        
        
        
        
        
        
#         def height(node):
#             if not node:
#                 return 0
#             elif not node.left and not node.right:
#                 return 1
#             return 1 + max(height(node.left), height(node.right))
        
#         def leaves(node):
#             if not node:
#                 return 0
#             elif not node.left and not node.right:
#                 return 1
#             else:
#                 return leaves(node.left) + leaves(node.right)
        
        
        
        
#         return self.sumNumbers(root.left) \
#                 + self.sumNumbers(root.right) \
#                 + root.val*( pow(10,height(root.left)) * leaves(root.left) + pow(10,height(root.right)) * leaves(root.right))
            
            