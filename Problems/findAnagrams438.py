"""
Solved using using a sliding window approach combined with a hashmap to track character frequencies.
A two-pointer approach + siliding window is also efficient.

We need to define the initial window. Here, the initial window is the first "len(p)" characters of "s".

We need to compare the frequency counts of characters in the initial window with the frequency counts of 
characters in the pattern "p" to check if they're anagrams.


i - len(p): Index of the character just before the window starts
i - len(p) + 1: Actual starting index of the window

"""

class Solution:
	def findAnagram(self, s, p):
		result = []
		p_counter = Counter(p)
		s_counter = Counter(s[:[len(p)]])

		if s_counter == p_counter:
			result.append(0)

		for i in range(len(p), len(s)):
			# Remove the leftmost character from the window
			if s_counter[s[i - len(p)]] == 1:
				del s_counter[s[i - len(p)]]
			else:
				s_counter[s[i - len(p)]] -= 1

			# Add the new character to the window
			if s[i] in s_counter:
				s_counter[s[i]] += 1
			else:
				s_counter[s[i]] -= 1

			# Check if the current window is an anagram of p
			if s_counter == p_counter:
				result.append(i - len(p) + 1)

		return result

