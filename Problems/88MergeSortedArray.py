"""
Solved using a two-pointer approach. Backward merging to avoid overwriting so largest elements are 
placed first, starting from the end of nums1. The last n elements are initially set to zeron helps to
make use of the extra space.
"""

from typing import List

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		p1, p2, p = m -1, n-1, m + n - 1
		while p1 >= p2:
			if nums1[p1] > nums2[p2]:
				nums1[p] = nums1[p1]
				p1 -= 1
			else:
				nums1[p] = nums2[p2]
				p2 -= 1
			p -= 1
		
		# If there are elements remaining in nums2
		while p2 >= 0:
			nums1[p] = nums2[p2]
			p2 -= 1
			p -= 1
	
