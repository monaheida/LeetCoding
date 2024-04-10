"""
Solved using a recursive approach.

"""
class Node:
	def __init__(self, value=None, children=None):
		self.value = value
		self.children = [] if children is None else children


class Solution:
	def cloneTree(self, root: 'Node') -> 'Node':
		if not root:
			return None

		cloned_children = [self.cloneTree(child) for child in root.children]
		cloned_node = Node(root.value, cloned_children)
		
		return cloned_node
