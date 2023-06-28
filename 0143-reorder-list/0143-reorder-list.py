class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle point
        slow = head
        fast = head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

          
        # Reverse the second part of the list
        prev, curr = slow, slow.next
        
        while curr:
            buffer = curr.next
            curr.next = prev
            prev, curr = curr, buffer
        
        slow.next = None
        
        
        
        # merge two lists
        first = head
        second = prev
        while first and second:
            if first:
                buffer = first.next
                first.next = second
                first = buffer
            if second:
                buffer = second.next
                second.next = first
                second = buffer

        """
        Do not return anything, modify head in-place instead.
        """