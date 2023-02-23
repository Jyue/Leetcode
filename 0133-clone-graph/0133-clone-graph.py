"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.alreadyClone = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.alreadyClone:
            return self.alreadyClone[node]
        
       
        
        clone_node = Node(node.val, [])
        
        # The key is original node and value being the clone node.
        self.alreadyClone[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node
        