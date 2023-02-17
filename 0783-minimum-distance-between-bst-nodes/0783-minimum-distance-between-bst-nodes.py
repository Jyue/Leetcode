# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inorderList = []
        res = float(inf)
        def inorder(node):
            nonlocal res
            if node.left:
                inorder(node.left)
            inorderList.append(node.val)
            if len(inorderList) >= 2:
                res = min(res, inorderList[-1] - inorderList[-2])
            if node.right:
                inorder(node.right)
        inorder(root)
        # for i in range(len(inorderList)-1):
        #     res = min(res, inorderList[i+1] - inorderList[i])
        return res
            