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

......................................................................................

"""
FollowUp: Could you minimize the total number of operations done?

- By reducing the number of swap operations. Instead of swapping non-zero elements with zeros individually, 
  we can keep track of the last non-zero index encountered so far. Then, we only need to overwri.
  Then, we only need to overwrite the element at that index with the current non-zero element.
"""

class Solution:
	def moveZeros(self, nums:List[int]):
		last_index = 0

		for i in range(len(nums)):
			if nums[i] != 0:
				nums[last_index] = nums[i]
				if i != last_index:
					nums[i] = 0
				last_index += 1

