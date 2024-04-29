"""
Solved using backtracking and bit manipulation(efficient solution).


"""

from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		def backtrack(start, sub):
			res.append(sub[:])
			for i in range(start, len(nums)):
				sub.append(nums[i])
				backtrack(i + 1, sub)  # Explore further with the updated subset
				sub.pop()              # Remove the current element to try other subsets
		res = []
		backtrack(0, [])        # Start backtracking from the beginning of the list with an empty subset
		return res



# bit manipulation approach

from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		res = []

		for i in range(2**n):   # all possible combinations of binary digits from 0 to 2^n
			sub = []
			for j in range(n):  # Convert the decimal number i to its binary representation
				if (i >> j) & 1: 
					sub.append(nums[j])
			res.append(sub)
		return res

# We know that each subset can be represented by a unique combination of bits. 
# If an element is included in the subset, its corresponding bit is set to 1; otherwise, it's set to 0.
# We check if the j-th bit of i is set to 1. If it is --> the j-th element of nums should be included in the current subset.
# If the j-th bit of i is set, we append nums[j] to the current subset.
