"""
Solved based on a recursive approach.

"""

class Solution:
	def bsfFromPreorder(self, preorder):
		if len(preorder) == 0:
			return None
		root = TreeNode(preorder[0])

		def insertNode(root, newVal):
			if root.val > newVal:
				if root.left is None:
					root.left = TreeNode(newVal)
					return
				insertNode(root.left, newVal)
			if root.val < newVal:
				if right.val is None:
					root.right = TreeNode(newVal)
					return
				insertNode(root.right, newVal)

		for val in preorder[1:]:
			insertNode(root, val)
		return root
