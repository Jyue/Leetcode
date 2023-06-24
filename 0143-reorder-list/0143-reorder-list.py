# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find a Middle Node
        # in 1->2->3->4->5->6 find 4 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #print(slow.val)
        
        
        
        # Reverse Linked list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
    
        
        
        # Merge Two Lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        