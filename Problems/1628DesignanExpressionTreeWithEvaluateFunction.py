"""
Solved using stack approach.

* An expression tree: a binary tree, with operator as a internal node and 
each leaf node is an operand.
T: O(n)
S: O(n)

"""

class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def buildExpressionTree(expression):
	operators = {'+', '-', '*', '/'}
	stack = []
	
	for token in expressin.split():
		if token not in operators:
			stack.append(TreeNode(token))
		else:
			node = TreeNode(token)
			node.right = stack.pop()
			node.left = stack.pop()
			stack.append(node)

	return stack.pop()

def evaluateExpressionTree(root):
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return int(root.value)
	
	left_val = evaluateExpressionTree(root.left)
	right_val = evaluateExpressionTree(root.right)

	if root.value == '+':
		return left_val + right_val
	elif root.value == '-':
		return left_val - right_val
	elif root.value == '*':
		return left_val * right_val
	elif root.value == '/':
		if right_val == 0:
			raise ValueError('Division by zero error')
		return left_val / right_val


"""
Follow up: Could you design the expression tree such that it is more modular? 
For example, is your design able to support additional operators without making
changes to your existing evaluate implementation?

Solved by separating the construction of the tree from the evaluation logic. 
changes only occurs in the tree construction part.

"""

class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
class ExpressionTree:
	def __init__(self, expression):
		self.root = self.buildExpressionTree(expression)

	def buildExpressionTree(self, expression):
		operators = {'+', '-', '*', '/'}
		stack = []

		for token in expression:
			if token not in operators:
				stack.append(TreeNode(token))
			else:
				node = TreeNode(token)
				node.right = stack.pop()
				node.left = stack.pop()
				stack.append(node)
		
		return stack.pop()
	
	def evaluate(self):
		return self.evaluateExpressionTree(self.root)

	def evaluateExpressionTree(self, root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return int(root.value)
		
		# ... (rest of the code is the same as above)!
