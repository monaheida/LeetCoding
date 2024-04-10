"""
Solved using DFS by a recursive funtion.

"""
from typing import Optional, List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def splitBST(self, root: Optional[TreeNode], target: int)  -> List[Optional[TreeNode]]:
		def dfs(node):
			if not node:
				return [None, None]
			
			if node.val <= target:
				small, large = dfs(node.right)
				node.right = small

				return [node, great]
			else:
				small, large = dfs(node.left)
				node.left = large

				return [small, node]

		return dfs(root)
