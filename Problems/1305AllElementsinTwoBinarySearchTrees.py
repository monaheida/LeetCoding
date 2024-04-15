"""
Solved using inorder traversal method:
- Visit the left subtree.
- Visit the root node.
- Visit the right subtree.

"""
from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
		def inorder_traversal(root, result):
			if root:
				inorder_traversal(root.left, result)
				result.append(root.val)
				inorder_traversal(root.right, result)

		def merge_sorted_lists(list1, list2):
			merged = []
			i = j = 0
			while i < len(list1) and j < len(list2):
				if list1[i] < list2[j]:
					merged.append(list1[i])
					i += 1
				else:
				   merged.append(list2[j])
				   j += 1
			merged.extend(list1[i:])
			merged.extend(list2[j:])
			return merged

		def merge_trees(root1, root2):
			result1 = []
			result2 = []
			inorder_traversal(root, result1)
			inorder_traversal(root, result2)
			return merge_sorted_lists(result1, result2)

		return merge_trees(root1, root2)

			
