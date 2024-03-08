"""
You are given a binary tree. Apart from the left and right child pointers, 
each node in the given binary tree points to a random node in the given binary
tree. You are supposed to return a clone of the binary tree.
Cloning a binary tree =  deep copy of the input binary tree.
Note :
Two nodes may have the same value associated with them.
The root node will be fixed and will be provided in the function.

Solution:
BFS: process the tree node by node
Create a queue to store the original nodes and their corresponding copies.
Enqueue the root node of the original tree along with its corresponding copy.
Iterate through the queue:
	a.Dequeue a node and its copy.
	b. If the dequeued node has left and/or right children, enqueue them along with their copies.
	c.If the dequeued node has a random pointer, set the random pointer of its copy to point to
	the corresponding node's copy.
Continue until the queue is empty.
Return the root node of the copied tree.

"""

class Solution:
	def copyRandomBinaryTree(self, root):
		if not root:
			return None

		copy_dict = {root: NodeCopy(root.val)}
		queue = collections.deque([root])

		while queue:
			node = queue.popleft()

			if node.random and node.random not in copy_dict:
				copy_dict[node.random] = NodeCopy(node.random.val)

				queue.append(node.random)

			copy_dict[node].random = copy_dict.get(node.random, None)

			if node.left and node.left not in copy_dict:
				copy_dict[node_left] = NodeCopy(node.left.val)
				queue.append(node.left)

			copy_dict[node].left = copy_dict.get(node.left, Node)

			if node.right and node.right not in copy_dict:
				copy_dict[node.right] = NodeCopy(node.right.val)
				queue.append(node.right)

			copy_dict[node].right = copy_dict.get(node.right, None)


		return copy_dict[root]


# T: O(N)
# S: O(N) + O(N)
