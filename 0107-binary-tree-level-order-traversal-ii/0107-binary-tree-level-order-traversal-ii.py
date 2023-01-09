# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        level = 0
        res = deque([[root.val]])
        level_node = deque([root])
        
        
        while level_node:
            length = len(level_node)
            for _ in range(length):
                node = level_node.popleft()
                if node.left:
                    level_node.append(node.left)
                if node.right:
                    level_node.append(node.right) 
            if level_node:
                res.appendleft([node.val for node in level_node])
        return res
            
            
            
            
            