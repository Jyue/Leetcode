class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
	
	# Don't be intimidated by the length, it's literally three easy questions combined you get to learn
	# How to Find the Middle Node | Reverse A Linked List        | Merge Two Lists
	# Find Middle Node: # 876     | Reverse Linked List: #206    | Merge Two Sorted Lists: #21
	# It's one of the best linked list questions on here


		# **** Find Middle Node ****
		slow, fast = head, head
		while fast and fast.next:

			slow, fast = slow.next, fast.next.next       

		prev, current = None, slow.next
		# Using Example 2, node 3 will no longer point to 4, this splits the list in half
		slow.next = None
		# **** Reverse The Second Half ****
		while current:
			temp = current
			current = current.next
			temp.next = prev
			prev = temp

		# **** Merge The Lists Together ****

		dummy = curr = ListNode(0)
		# head1 will be the start of the first list (node 1)
		# head2 will be the start of the second list (node 5)
		head1, head2 = head, prev

		while head1 and head2:
			if head1:
				curr.next, head1 = head1, head1.next
				curr = curr.next

			if head2:
				curr.next, head2 = head2, head2.next 
				curr = curr.next

		# whichever head1 or head2 still has a node remaining, we point to that remaining node
		curr.next = head1 or head2

		"""
		Do not return anything, modify head in-place instead.
		"""