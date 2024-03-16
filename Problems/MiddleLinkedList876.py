"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

- Solving using a two-pointer (slow & fast) approach
  slow pointer moves one step at a time, fast pointer moves two steps at a time.
  faster pointer reaches the end of the list --> the slower pointer will be at the middle node.
"""

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
def find_middle(node):
	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	
	return slow



# Example Create the linked list: 1 -> 2 -> 3 -> 4 -> 5

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(6)

middle_node = find_middle(head)
print("Middle node value:", middle_node.val)
