"""
ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.

Solved using Stack

"""

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
		stack = []

		while head:
			srack.append(head)
			head = head.getNext()
		while stack:
			node = stack.pop()
			node.printValue()


# By pushing all the nodes onto the stack, the space occupied by the stack will be 
# proportional to the number of nodes in the linked list --> S: O(n)

# In the first loop, By traversing the linked list once to push all nodes onto the stack
# each node once visited --> T: O(n)



"""
Follow up, could you solve this problem in Constant space complexity?
Solved by the recursive approach

"""
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
		if not head:
			return
		self.printLinkedListInReverse(head.getNext())
		head.printValue()

