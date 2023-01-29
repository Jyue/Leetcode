# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        
        oldLast = head
        length = 1
        while oldLast.next:
            oldLast = oldLast.next
            length += 1
            
        # print(oldLast.val)
        newLastLoc = (length - k - 1) % length 
        
        newLast = head
        for i in range(newLastLoc):
            newLast = newLast.next
            
        # print(newLast.val)
        
        
        if newLast.next:
            newStart = newLast.next
        else:
            newStart = head
        
        oldLast.next = head
        newLast.next = None
        
        return newStart
        