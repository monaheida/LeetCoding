"""
Solved using a two-point appraoch! Hint1 is helpful to consider.

l = 1: the first element of the array is always unique in a sorted array ==> the position l 
starts from the second element (index 1).

"""
from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums:
			return 0
		
		l = 1
		for l in range(1, len(nums)):
			if nums[r] != nums[r-1]:
				nums[l] = nums[r]
				l += 1
		
		return l
