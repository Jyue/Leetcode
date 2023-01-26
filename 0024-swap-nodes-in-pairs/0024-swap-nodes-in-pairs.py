# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        first_node = head
        second_node = head.next
        
        futureHead = head.next.next
        second_node.next = head
        first_node.next = self.swapPairs(futureHead)
        
        return second_node