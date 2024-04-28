"""
Solved using backtracking

By swapping elements at indices first and i, the code ensures that every possible permutation 
of the elements in the nums array is generated during the backtracking process. 

"""

from typing import List

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		def backtrack(first=0):
			if first == n:
				permutations.append(nums[:])
			for i in range(first, n):
				nums[first], nums[i] = nums[i], nums[first]
				backtrack(first + 1)
				nusm[first], nums[i] = nums[i], nums[first]

		n = len(nums)
		permutatios = []
		backtrack()
		return permutations

