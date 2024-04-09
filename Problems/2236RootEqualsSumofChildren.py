"""
Solved using just a simple checking approach.

"""

class Solution:
	def checkTree(self, root):
		if root is None:
			return False
		if root.left is None and root.right is None:
			return True
		left_val = root.left.val if root.left else 0
		right_val = root.right.val if root.right else 0

		return root.val == left.val + right.val
