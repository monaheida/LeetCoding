"""
Solved using memoization approach.

T: O(2^n)
Time complexity depends on the number of unique binary trees that can be formed with n nodes.
Since each node can be either a left child, a right child, or a root, the number of unique binary trees grows exponentially with n.

S: O(n)
memo stores the results of subproblems to avoid redundant calculations.
The maximum depth of recursion and the number of entries in the memoization dictionary is proportional to n.

"""

from typing import List

class Solution:
	def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
		if n % 2 == 0:
			return [] # Number of nodes in a full binary tree must be odd
		
		memo = {}

		def generate_tree(n):
			if n in memo:
				return memo[n]

			list = []
			if n == 1:
				list.append(TreeNode(0))
			else:
				for i in range(1, n-1, 2):
					l_Trees = _allPossibleFBT(i)
					r_Trees = _allPossibleFBT(n-1-i)

					for lt in l_Trees:
						for rt in r_Trees:
							list.append(TreeNode(0, lt, rt))

			memo[n] = list
			return list

		return _allPossibleFBT(n)


