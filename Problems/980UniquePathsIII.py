"""
Explanation: 
	start: th line finds the starting square coordinates (start) by iterating over all the rows and columns.
	It creates a tuple of coordinates (r, c) where the value in the grid is 1 (indicating the starting point).
	The [0] at the end extracts the first tuple found.
	
	Using *start:  unpacking the tuple start into individual arguments. dfs(*start, zeros) is equivalent to 
	dfs(row, col, zeros).
	
"""

class Solution:
	def uniquePathsIII(self, grid: List[List[int]]) -> int:
		M, N = range(len(grid)), range(len(grid[0]))
		zeros = sum(row.count(0) for row in grid)       # calculates the total number of empty squares (zeros) in the grid

		start = tuple((r, c) for r in M for c in N if grid[r][c] == 1)[0]

		self.ans = 0

		def dfs(row, col, zeros):
			grid[row][col] = 3    # current cell as visited by setting its value to 3
			for dr, dc in ((-1,0),(0,-1),(1,0),(0,1)):     # iterates over all possible directions: up, left, down, and right
				R, C = row+dc, row+dc    # calculates the new row R and column C based on the current position (row, col) and the direction (dr, dc)

				if R in M and C in N:
					if grid[R][C] == 0:
						dfs(R, C, zeros-1)
					if grid[R][C] == 2 and zeros == 0:
						self.ans += 1

			grid[row][col] = 0
			return
		
		dfs(*start, zeros)
		return self.ans






