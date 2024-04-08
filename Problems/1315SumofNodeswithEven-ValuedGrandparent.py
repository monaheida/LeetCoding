"""
Solved usign recursive approach.

T: O(n)
S: O(n)

"""

class Solution:
	def sumEvenGrandparent(self, root):
		def dfs(node, parent, grandparent):
			if not node:
				return 0
			total = 0

			if grandparent and grandparent.val % 2 == 0:
				total += node.val

			total += dfs(node.left, node, parent)
			total += dfs(node.right, node, parent)
			return total
		
		# None is passed as the parent and grandparent for the root node because it has no parent or grandparent (it's the root).
		return dfs(root, None, None)

