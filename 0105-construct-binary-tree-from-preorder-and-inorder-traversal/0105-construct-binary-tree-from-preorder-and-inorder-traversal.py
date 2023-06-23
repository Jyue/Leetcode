# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse()
        return self.buildTreeRec(preorder, inorder)
    def buildTreeRec(self, preorder, inorder):
        if not inorder: return None
        n = TreeNode(preorder.pop())
        i = inorder.index(n.val)
        n.left = self.buildTreeRec(preorder, inorder[:i])
        n.right = self.buildTreeRec(preorder, inorder[i+1:])
        return n