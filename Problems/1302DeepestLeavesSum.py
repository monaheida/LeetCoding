"""
Solved using DFS traversal of binary tree.


"""

class Solution:
	def deepestLeavesSum(self, root):
		max_depth = 0
		deepest_sum = 0

		def dfs(node, depth):
			nonlocal max_depth, deepest_sum

			if not node:
				return 0

			if depth > max_depth:
				max_depth = depth
				# When the DFS traversal a leaf node at the deepest level (there are no children nodes below it), we initialize deepest_sum with the value of that leaf node (node.val). 
				deepest_sum = node.val
			elif depth == max_depth:
				deepest_sum += node.val

			# 0 is the initial depth of the root node. The depth is passed as an argument to keep track of the level or depth of each node during traversal.
			dfs(root, 0)
			return deepsest_sum
