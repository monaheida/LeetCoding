"""
Solved using heap.
- Creating a list of tuples, each tuple contains the negative frequency (to simulate a max heap)
  and the character.

T: O(n log k)  
n: length of the input string
k: number of unique characters in the string

"""

class Solution:
	def frequencySort(self, s: str) -> str:
		freq_map = {}
		max_heap = [(-freq, char) for char, freq in freq_map.items()]
		heapq.heapify(max_heap)

		sorted_string = ''
		while max_heap:
			freq, char = heapq.heappop(max_heap)
			sorted_string += char * (-freq)

		return sorted_string


