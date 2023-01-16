# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return head.next
        
        p = ListNode(-1)
        p.next = head
        q = head
        for _ in range(n-1):
            q = q.next
        while q.next:
            q = q.next
            p = p.next
        print(p.val,q.val)
        if p.next.next:
            p.next = p.next.next
        else:
            p.next = None
        # print(p.next.val)
        return head.next if p.val == -1 else head
        