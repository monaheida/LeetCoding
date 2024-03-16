"""

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

We can solve it using a hash map and a two-pointer approach.
A two-pointer approach doesn't handle negative numbers well.

But if constraints such as non-negative numbers are given so we can't solve it using a two-pointer approach!

"""

class Solution:
	def subarraySum(nums, k):
		count = 0
		current_sum = 0
		prefix_sum = {0:1}

		for num in nums:
			current_sum += 1
			complement = current_sum - k
			if complement in prefix_sum:
				count += prefix_sum[complement]
			prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

		return count




# T: O(n)  We only iterate through the array once
# S: O(n)  Because the prefix_sum dictionary can contain all the prefix sums in the array, up to the length of the array.
