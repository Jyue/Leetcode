"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        result = [[root.val]]
        level = 0
        node_num = 1
        
        level_nodes = deque([root])
        while level_nodes:
            level_nodes_val = []
            for _ in range(node_num):
                node = level_nodes.popleft()
                for child in node.children:
                    level_nodes.append(child)
                    level_nodes_val.append(child.val)
                    
            node_num = len(level_nodes)
            if level_nodes_val:
                result.append(level_nodes_val)

        return result