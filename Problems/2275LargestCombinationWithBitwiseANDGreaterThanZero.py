"""
In binary representation, a value of 1 corresponds to the rightmost bit being set, and shifting
it to the left by one bit (i = i << 1) represents moving to the next bit position towards the left. 
This process continues until i represents the leftmost bit position.

"""
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
		max_elm = max(candidates)

		i = 1
		res = 0
		while i <= max_elm:
			current = 0
			for c in candidates:
				if i & c == i:
					current += 1

			res = max(res, current)
			i = i << 1
		
		return res

