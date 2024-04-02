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


# recursively building the max binary tree by iterating over each element in the input list nums.
# At each level of recursion, the function performs a linear search to find the max val in the current sublist, which takes O(n) time
# at each level, the size of the sublist is reduced by approximately half (assuming the elements are evenly distributed)!
# T: O(n logn)

# the recursion stack space used during the recursive calls
# At each recursive call, additional stack space is used to store the function call and local variables, including the sublist of nums.
# the function is called recursively for each partitioned sublist --> max depth of recursion: O(log n).
# S: O(logn)

