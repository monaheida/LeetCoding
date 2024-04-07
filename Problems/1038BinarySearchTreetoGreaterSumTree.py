"""
Solved using DFS of the BST:
(visit nodes in descending order (right, root, left))
- recursively traverse the right subtree.
- At each node, update its value by adding the sum of all greater values.
- recursively traverse the left subtree.

The reverse_inorder function: a helper function, traverse BST in reverse inordern.

In a regular inorder traversal, the nodes of a BST are visited in ascending order, 
in a reverse inorder traversal, the nodes are visited in descending order.

T: O(n)

The space complexity is determined by the recursive calls made during the reverse inorder traversal.
the recursion depth is proportional to the height of the BST --> S: O(h), h: height of the tree.
In the worst-case scenario: the tree is skewed (linked list), the height of the tree is O(n), S: O(n).
In the best-case scenario: the tree is balanced, the height of the tree is O(log n), S: O(log n).

S: ranges from O(log n) to O(n)

"""

class Solution:
	def bstToGST(self, root):
		total = 0
		
		def reverse_inorder(node):
			nonlocal total
			if node:
				reverse_inorder(node.right)
				total += node.val
				node.val = total
				reverse_inorder(node.left)

		reverse_inorder(root)
		return root



