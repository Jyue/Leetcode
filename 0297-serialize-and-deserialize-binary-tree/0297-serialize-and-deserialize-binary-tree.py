# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque()
        queue.append(root)
        res = ''
        while queue:
            node = queue.popleft()
            if not node:
                res += 'None,'
            else:
                res += str(node.val)+','
                queue.append(node.left)
                queue.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodeList = data.split(',')
        root = TreeNode(int(nodeList[0]))
        queue = deque([root])
        
        i = 1
        while queue and i < len(nodeList):
            node = queue.popleft()
            if nodeList[i] != 'None':
                left = TreeNode(int(nodeList[i]))
                node.left = left
                queue.append(left)
            i += 1
            if nodeList[i] != 'None':
                right = TreeNode(int(nodeList[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root
             

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))