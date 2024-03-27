"""
Solving using sliding window approach (defining a window in this case, a substring of length K) 
and moving it across the string "s" one character at a time to examine all possible substrings.


Time Complexity: O(n)


Space Complexity: O(1)

The algorithm uses a Counter to keep track of the frequency of characters within the sliding window.
The space required for this counter is O(26), as there are 26 lowercase English letters.
This is constant space and can be considered O(1).
The space required for other variables such as num_substrings, start_idx, and end_idx
is also constant and is O(1).

"""

class Solution:
	def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
		s_length = len(s)
		if k > s_length or k > 26:
			return 0

		num_substrings = start_idx = 0
		char_freq = Counter()

		for end_idx, char in enumerate(s):
			char_freq[char] += 1

			while char_freq[char] > 1 or end_idx - start_idx + 1 > k:
				char_freq[s[start_idx]] -= 1
				start_idx += 1

			if end_idx - start_idx + 1 == k:
				num_substrings += 1

		return num_substrings


