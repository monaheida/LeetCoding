"""
zip(*grid): transposes the grid.
*grid: unpack the grid, passing each row of the grid as a separate argument to zip().
zip() then pairs up the elements at corresponding positions from each row, effectively transposing the grid.

"""

from typing import List

class Solution:
	def deleteGreatestValue(self, grid: List[List[int]]) -> int:
		for i in range(len(grid)):
			gird[i].sort()
		grid = list(zip(*grid))

		return sum(max(row) for row in grid)
