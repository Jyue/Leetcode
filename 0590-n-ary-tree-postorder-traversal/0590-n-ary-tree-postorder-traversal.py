"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def dfs(node):
            
            if not node:
                return
            if not node.children:
                
                res.append(node.val)
                return
            
            for child in node.children:
                dfs(child)
            res.append(node.val)
                
        res = []
        dfs(root)
        return res