# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        # print(fast.val)
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # print(slow.val, fast.val)
        slow.next = slow.next.next
        return head
        