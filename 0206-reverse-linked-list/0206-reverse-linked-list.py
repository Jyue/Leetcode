# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(prev, curr, next_):
            curr.next = prev
            return reverse(curr, next_, next_.next) if next_ else curr

                
                
        if not head or not head.next:
            return head
        
        

        if head.next:
            last = reverse(head, head.next, head.next.next)    
            
        head.next = None
        
        return last