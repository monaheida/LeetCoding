"""
Solving using helps reducing the time complexity to O(N) by allowing all computation
to be done within 1 traversal of the loop instead of having a nested traversal.

"""

def longest_substring_length(s):
	if not s:
		return 0

	char_index = {}    # Dic to store the most recent index of each char
	max_length = start = 0
	
	for i, char in enumerate(s):
		if char in char_index and char_index[char] >= start:
			start = char_index[char] + 1    # Update the start index if the char repeats
		else:
			max_length = max(max_length, i - start + 1)

		char_index[char] = i

	return max_length


s = "abcabcbb"
print(longest_substring_length(s))




