"""
Solved using a two-pointer approach.

"pairSum" method takes a singly-linked list as input, returns the maximum sum of pairs of nodes,
where one node is from the first half of the list and the other node is from the second half of the list.

If we don't reverse the second half, we would need to iterate through the first half from the beginning while
simultaneously iterating through the second half from the end. This would require either storing the nodes in 
the second half in a separate data structure (like an array) or using recursion to traverse the list backward.

T: O(n)  traversing the list multiple times (to count the nodes, to find the middle, to reverse the second half,
and finally to compute the sum), each taking O(n)

S: O(1) only uses a constant amount of additional space for pointers and variables, regardless of the input size.

"""

class Solution:
	def pairSum(self, head):
		head = pointer
		count = 0
		while pointer:
			pointer = pointer.next
			count += 1

		middle = count // 2
		
		# Creating second linked list from middle:
		half = None
		curr = head
		track = 0
		while curr:
			if track == middle:
				half = curr
			curr = curr.next
			track += 1

		# reversing the second half
		reversed_half = None
		curr_half = half
		while curr_half:
			nxt = curr_half.next
			curr_half.next = reversed_half
			reversed_half = curr_half
			curr_half = nxt

		# computing max twin sum
		res = 0
		original = head
		while reversed_half:
			curr_sum = reversed_half.val + original.val
			res = max(res, curr_sum)
			reversed_half = reversed_half.next
			original = original.next

		return res

		
