# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # First, create a dictionary
        # key: values in preorder, value: the index of values in inorder.
        inIndexDict = dict()
        for index, value in enumerate(inorder):
            inIndexDict[value] = index
        def recur(i, left, right):
            if left > right:
                return
            curVal = preorder[i]
            newNode = TreeNode(curVal)
            newNode.left = recur(i + 1, left, inIndexDict[curVal] - 1)
            newNode.right = recur(i + inIndexDict[curVal] - left + 1, inIndexDict[curVal] + 1, right)
            return newNode
        return recur(0, 0, len(inorder) - 1)