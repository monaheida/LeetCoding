"""
Solution: (Based on backtracking) A DFS approach to traverse the DAG.

- Start at the source node (node 0).
- Explore all possible paths by recursively visiting each neighbor of the current node.
- If we reach the target node (last node in the graph), we add the current path to the list of paths.
- If: a node with no outgoing edges --> backtrack by removing the last node from the current path
  and continuing the search from the previous node.

* Backtracking involves removing the last node from the current path and
  returning to the previous node to explore other neighboring nodes.

"""

from typing impor List

class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		def dfs(node, path):
			if node == len(graph) - 1:    # target node the last node in the graph
				paths.append(path[:])
				return

			for neighbor in graph[node]:  # Explore all neighbors of the current node
				path.append(neighbor)
				dfs(neighbor, path)
				path.pop()       # Backtrack: Remove the neighbor from the path

			paths = []
			dfs(0, [0])

			return paths
