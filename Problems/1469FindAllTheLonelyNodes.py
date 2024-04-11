"""
Solved using DFS. Traversing the tree starting from the root
and check at each node if it has any lonely children. 

"""
from typing import Optional, List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
		def dfs(node):
			if node is None or (node.left is None and node.right is None):
				return

			if node.left is None:
				lonely_nodes.append(node.right.val)

			if node.right is None:
				lonely_nodes.append(node.left.val)

			dfs(node.left)
			dfs(node.right)

		lonely_nodes = []
		dfs(root)

		return lonely_nodes



