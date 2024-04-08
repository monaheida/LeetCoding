"""
Solved using Depth First Search implemented by recursive approch.

T: O(n)
S: O(n) because it utilizes recursion for the dfs, which can go as deep as the height of the binary tree. 

"""
class Solution:
	def averageOfSubtree(self, root):
		res = 0

		def dfs(node):
			nonlocal res

			if not node:
				return 0, 0

			left_sum, left_count = dfs(node.left)
			right_sum, right_count = dfs(node.right)
			
			# Calculate the sum and count of the current subtree
			curr_sum = node.val + left_sum + right_sum
			curr_count = 1 + left_count + right_count

			if curr_sum // curr_count == node.val:
				res += 1

			return curr_sum, curr_count
	
		dfs(root)
		return res
