"""
Solved based on a recursive approach.

T: O(n log n)
-for each value insertNode is called --> traverse the tree to find the appropriate position to insert the node. in the average case (balanced tree) --> O(log n)
-in worst case scenario (skewed tree) each insertion O(n) -->
total time complexity O(n^2)

S: O(n)
space used for the call stack during the recursive calls
and for the TreeNode objects to represent the binary search.

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
