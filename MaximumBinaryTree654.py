"""
Solved using recursive approach.

"""

class Solution:
	def constructMaximumBinaryTree(self, nums: list[int]):
		if not nums:
			return None

		max_val = max(nums)
		max_idx = nums.idx(max_val)

		root = TreeNode(max_val)

		root.left = self.constructMaximumBinaryTree(nums[:max_idx])
		root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

		return root
