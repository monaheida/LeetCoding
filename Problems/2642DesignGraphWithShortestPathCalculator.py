"""
Solved using Dijkstra's algorithm.
Start by initializing a priority queue (often implemented with a min-heap) 
to store nodes that need to be explored. 

"""

from typing import List

class Graph:
	def __init__(self, n: int, edges: List[List[int]]):
		self.graph = {}
		for from_node, to_node, cost in edges:
			if from_node not in self.graph:
				self.graph[from_node] = []
			self.graph[from_node].append((to_node, cost))

	
	def addEdge(self, edge: List[int]) -> None:
		from_node, to_node, cost = edge
		if from_node not in self.graph:
			self.graph[from_node] = []
		self.graph[from_node].append((to_node, cost))

	
	def shortestPath(self, node1: int, node2: int) -> int:
		pq = [(0, node1)]
		distances = {node1: 0}

		while pq:
			dist, node = heapq.heappop(pq)

			if node == node2:
				return dist

			if dist > distances[node]:
				continue

			if node in self.graph:
				for neighbor, cost in self.graph[node]:
					new_dist = dist + cost
					if neighbor not in distances or new_dist < distances[neighbor]:
						distances[neighbor] = new_dist
						heapq.heappush(pq, (new_dist, neighbor))

		return -1

