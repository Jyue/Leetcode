class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1. 找中間點
        slow = head
        fast = head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            
        # 2. 反轉後半段
        prev, curr = slow, slow.next
        

        while curr:
            buffer = curr.next
        
            curr.next = prev

            prev, curr = curr, buffer
            
        slow.next = None
        
        # 3. 合併
        # 利用兩個指標 first 和 second 分別指向左側和反轉的右側之頭，
        # 然後再定義一個暫存用的指標 buffer，接著做以下步驟直到兩者都掃完為止：
        # 因為等等會動到 first->next，所以先用 buffer 來保留 first->next 之內容。
        # 因此接著把 first->next 指向 second。
        # 最後把 first 指向 buffer（即原 first->next）；
        # (second也是)
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