"""
Solving using a two-pointer approach

"""

class solution:
	def twoSum(self, numbers, target):
		left, rigth = 0, len(numbers)-1

		while left < right:
			toatl = numbers[left] + numbers[right]

			if total == target:
				return [left + 1, right + 1,]
			elif total < target:
				left += 1
			else:
				right -= 1

		return target




# S: O(1)  the solution only requires a few integer variables (left, right, total)
# T: O(n)
