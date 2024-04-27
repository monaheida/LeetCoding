"""
Using a bitmask (a binary pattern used for bitwise operations, where each bit represents
a specific boolean attribute or condition).

Here the bitmask is used to represent all possible subsets of a given list of integers.
Each bit in the bitmask corresponds to whether or not the element at that position in the list is included in a subset.

we want subsets excluding the empty subset, which has no elements 
--> we subtract 1 from the length of the list (len(nums) - 1) to exclude the empty subset.

"""
from typing import List

class Solution:
	def subsetXORSum(self, nums: List[int]) -> int:
		res = 0
		for num in nums:
			res |= num
		return res * (1 << (len(nums) - 1))
