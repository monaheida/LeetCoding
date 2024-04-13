"""
Solved using inorder traversal method.
- Start at the root node (or any node in the tree).
- Recursively traverse the left subtree.
- Visit the current node.
- Recursively traverse the right subtree.

"""

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		def balanced_bst(nodes):
			if not nodes:
				return None

			mid = len(nodes) // 2
			root = TreeNode(node[mid].val)
			root.left = balanced_bst(nodes[:mid])
			root.right = balanced_bst(nodes[mid+1:])
			return root

		def inorder_traversal(node):
			if not node:
				return []
			return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)

		# Perform inorder traversal to get sorted list of nodes
		sorted_nodes = inorder_traversal(root)

		return balanced_bst(sorted_nodes)
