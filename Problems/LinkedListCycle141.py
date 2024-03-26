"""
The sliding window technique is typically used in array-based problems.
For linked list problems like detecting cycles,the two pointers approach is generally more suitable and efficient.

The two pointers approach has a time complexity of O(n) and a space complexity of O(1).

"""

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def hasCycle(head):
		slow = fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True

		return False
				
