"""
Solving using sliding window approach (defining a window in this case, a substring of length K) 
and moving it across the string "s" one character at a time to examine all possible substrings.


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


