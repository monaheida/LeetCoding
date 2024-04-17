"""
Solved using heap (allows for constant time retrieval of the minimum (or maximum) element.
This is crucial for this problem because both Alice and Bob need to select the smallest number from the remaining numbers in each turn).
Heaps maintain a partially sorted order. When elements are added or removed, 
the heap property ensures that the smallest (or largest) element is always at the root.

"""

from typing import List

class Solution:
	def numberGame(self, nums: List[int]) -> List[int]:
		heap = nums[:]
		heapq.heapify(heap)

		arr = []
		
		while heap:
			Alice_move = heapq.heappop(heap)
			Bob_move = heapq.heappop(heap)

			arr.append(Bob_move)
			arr.append(Alice_move)

		return arr
