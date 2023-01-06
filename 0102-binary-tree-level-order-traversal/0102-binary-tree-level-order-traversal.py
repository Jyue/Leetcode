# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        
        res = []
        level_node = []
        level_count = 0
        
        # Base Case
        if not root :
            return []
        
        
        
        else:
            deq = deque([root,])
        # print(deq)
        
       
        while deq:
            res.append([])
            level_length = len(deq)
            
            for _ in range(level_length):
                node = deq.popleft()
                # fulfill the current level
                res[level_count].append(node.val)
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        
            # print(res)
            
            
            level_count += 1
            
            
        
        return res