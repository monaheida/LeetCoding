"""
Solved using stack approach

"""

class Solution:
	def removeOuterParentheses(self, S):
		res = ""
		stack = []

		for char in S:
			if char == '(':
				if stack:
					res += char
				stack.append(char)

			else:
				stack.pop()
				if stack:
					res += char
		
		return res


"""
The function iterates through each character of the input string once -->  T: O(n)

If all parentheses are opening parentheses and the stack grows to its maximum size
(which is the length of the input string s) --> S: O(n).

"""
