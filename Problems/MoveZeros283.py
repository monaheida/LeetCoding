"""
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Soving using a two-pointer approach!
- One pointer iterate through the array,
- the other pointer keeps track of the position to place the next non-zero element.

"""


class Solution:
	def moveZeros(self, nums:List[int]):
		
		index = 0

		for i in range(len(nums)):
			if nums[i] != 0:
				# swapping nums[i] with nums[index] ---> move the current non-zero element to the correct position determined by index
				nums[i], nums[index] = nums[index], nums[i]

				index += 1






# T: O(n)
# iteration through the array once using a single loop
# in each iteration: constant-time operations (comparisons and swapping)

# S: O(1)
# space is constant regardless the size of the array

