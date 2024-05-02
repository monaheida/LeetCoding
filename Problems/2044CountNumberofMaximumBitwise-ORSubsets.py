"""
DP approch.

"""

class Solution:
	def countMaxOrSubsets(self, nums: List[int]) -> int:
		max_or = 0
		max_count = 0
		dp = {0: 1}     # counts of subsets with each OR value

		for num in nums:
			new_dp = dp.copy()   # to avoid modifying it while iterating
			for key in dp:
				new_or = key | num
				new_dp[new_or] = new_dp.get(new_or, 0) + dp[key]
			dp = new_dp

		for key, value in dp.items():
			if key > max_or:
				max_or = key
				max_count = value
			elif key == max_or:
				max_count += value	
