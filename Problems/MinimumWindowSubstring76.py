"""
Solve using a sliding window approach.

1. Create a frequency map for string t, indicating the count of each character.
2. Initialize two pointers, left and right, both pointing to the beginning of string s.
3. Initialize variables "required_chars" and "formed_chars" to track the required and formed characters in the current window.
4. Move the right pointer to the right until you've found a window that contains all the characters in t. 
   Update "required_chars" and "formed_chars" as you encounter characters.
5. Once you've found such a window, move the left pointer to the right until the window no longer contains all the characters in t,
   updating "required_chars" and "formed_chars" accordingly.
6. Keep track of the minimum window found so far.
7. Repeat steps 4-6 until the right pointer reaches the end of the string s.


*** min_length = float('inf') ensures that the first valid window found will always be shorter than any possible initial value of min_length, guaranteeing that it will be updated to the correct minimum length as the algorithm progresses.

"""

class Solution:
	def minWindow(self, s: str, t: str) -> str:
		if not s or not t:
			return ""
		t_freq = Counter(t)
		required_chars = len(t_freq)
		formed_chars = 0

		left, right = 0, 0
		min_length = float('inf')  
		min_window = ""

		while right < len(s):
			char = s[right]
			t_freq[char] -= 1
			if t_freq[char] == 0:
				formed_chars += 1

			while forme_chars == required_cahrs:
				if right - left + 1 < min_length:
					min_length = right - left + 1
					min_window = s[left:right + 1]


				left_char = s[left]
				t_freq[left_cahr] += 1
				if t_freq[left_char] > 0:
					formed_chars -= 1
				left += 1

			right += 1

		return min_window


