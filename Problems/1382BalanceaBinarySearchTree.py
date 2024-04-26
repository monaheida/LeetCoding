"""
Solved using an in-order traversal method.
- Traverse the left subtree recursively.
- Visit the current node.
- Traverse the right subtree recursively.

"""

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = val

class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		def buildBalancedBST(nodes):
			if not node:
				return None

			mid = len(nodes) // 2
			root = TreeNode(nodes[mid].val)
			root.left = buildBalancedBST(nodes[:mid])
			root.right = buildBalancedBST(nodes[mid+1:])
			return root

		def inorder_traversal(node):
			if not node:
				return []
			return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)
		
		# Perform inorder traversal to get sorted list of nodes
		sorted_nodes = inorder_traversal(root)

		return buildBalancedBST(sorted_nodes)


