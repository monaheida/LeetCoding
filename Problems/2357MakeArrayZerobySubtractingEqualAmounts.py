"""
 Counting the number of unique non-zero elements in the array -->  effectively represents 
 the minimum number of operations required to make all elements zero.
- converts the input list "nums" to a set to remove duplicate elements.
- subtracts the {0} set from the set of unique elements, effectively removing the zero element.
- returns the length of the resulting set --> the count of unique non-zero elements.

* Sets in Python do not allow duplicate elements, so any duplicate elements in the list will be removed. 

"""
from typing import List

class Solution:
	def minimumOperations(self, nums: List[int]) -> int:
		return len(set(nums) - {0})
