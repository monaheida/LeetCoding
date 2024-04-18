"""
Solved by iterating through each row, counting the number of soldiers,
and then sorting the rows based on the number of soldiers and their indices.

"""

from typing import List

class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		soldiers_count = [(sum(row), i) for i, row in enumerate(mat)]
		soldiers_count.sort()

		return [i for _, i in soldiers_count[:k]]


