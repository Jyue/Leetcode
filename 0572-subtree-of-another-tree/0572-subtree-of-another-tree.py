# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False
    
    
    def traverse_tree(self, s):
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None