# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        # 技巧: dummy node
        dummy = ListNode(-1)
        p = dummy
        
        # 如何快速得到 k 個節點中的最小節點，接到結果list上？ ⇒ Min-Heap
        pq = []
        seq = 0
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, seq, head))
                seq += 1

        while pq:
            # 獲取最小節點，接到結果list上
            node = heapq.heappop(pq)[2]
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, seq, node.next))
                seq += 1
            # p 指針不斷推進
            p = p.next
        return dummy.next
    